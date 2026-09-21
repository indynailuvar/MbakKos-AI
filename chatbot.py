import os
import json

from dotenv import load_dotenv
from groq import Groq

from prompt import SYSTEM_PROMPT


# =========================
# LOAD API
# =========================

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



# =========================
# FILE
# =========================

HISTORY_FILE = "chat_history.json"

FOOD_FILE = "food_database.json"



# =========================
# LOAD DATABASE MAKANAN
# =========================

def load_food_database():

    with open(
        FOOD_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



food_database = load_food_database()



# =========================
# DETEKSI BAHAN
# =========================

def detect_food(text):

    """
    Mendeteksi bahan dari input user
    menggunakan alias.
    """

    hasil = []

    text = text.lower()


    for kategori in food_database:

        for nama_bahan, data in food_database[kategori].items():


            for alias in data["alias"]:


                if alias in text:


                    if nama_bahan not in hasil:

                        hasil.append(nama_bahan)


    return hasil




# =========================
# AMBIL HARGA BAHAN
# =========================

def get_food_price(ingredients):


    daftar_harga = []


    total = 0


    for item in ingredients:


        for kategori in food_database:


            if item in food_database[kategori]:


                harga = food_database[kategori][item]["harga"]


                daftar_harga.append(

                    {
                        "nama": item,
                        "harga": harga
                    }

                )


                total += harga



    return daftar_harga, total




# =========================
# LOAD HISTORY
# =========================

def load_history():


    if os.path.exists(HISTORY_FILE):


        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:


            return json.load(file)



    return [

        {
            "role":"system",
            "content":SYSTEM_PROMPT
        }

    ]




# =========================
# SAVE HISTORY
# =========================

def save_history(history):


    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(

            history,

            file,

            indent=4,

            ensure_ascii=False

        )




# =========================
# CHAT STREAMING
# =========================

def chat_stream(
        message,
        user_data,
        mode
):


    history = load_history()



    # cari bahan

    ingredients = detect_food(message)



    if ingredients:

        user_data["ingredients"] = ingredients




    # hitung harga

    detail_harga, total = get_food_price(

        user_data["ingredients"]

    )



    user_data["estimated_cost"] = total




    context = f"""

INFORMASI PENGGUNA:

Mode:
{mode}


Budget:
Rp{user_data.get('budget',0)}


Bahan tersedia:

{user_data['ingredients']}


Harga bahan:

{detail_harga}


Estimasi maksimal bahan:
Rp{total}



ATURAN TAMBAHAN:

Gunakan hanya bahan yang tersedia.

Jangan menambahkan bahan baru.

Jika membutuhkan tambahan:
hanya gunakan bumbu dasar.

"""



    history.append(

        {

            "role":"user",

            "content":

            message + context

        }

    )



    try:


        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=history,

            temperature=0.5,

            stream=True

        )



        jawaban = ""



        for chunk in response:


            token = chunk.choices[0].delta.content



            if token:


                jawaban += token


                yield token




        history.append(

            {

                "role":"assistant",

                "content":jawaban

            }

        )



        save_history(history)



    except Exception as error:


        yield f"""

Maaf, sedang ada gangguan koneksi AI.

Error:
{error}

"""




# =========================
# RESET
# =========================

def reset_history():


    if os.path.exists(HISTORY_FILE):

        os.remove(HISTORY_FILE)