import streamlit as st

from chatbot import (
    chat_stream,
    reset_history
)



# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(

    page_title="Mbak Kos AI",

    page_icon="🍚",

    layout="wide"

)



# ==========================================
# HEADER
# ==========================================

st.title("🍚 Mbak Kos AI")

st.caption(
    "Smart Meal Planner untuk mahasiswa dan anak kos"
)


st.write(
    """
Halo! Saya Mbak Kos AI.

Saya membantu kamu menentukan menu hemat
berdasarkan budget, bahan yang tersedia,
dan kondisi memasak kamu.
"""
)



# ==========================================
# SESSION STATE
# ==========================================


# menyimpan chat

if "messages" not in st.session_state:

    st.session_state.messages = []



# menyimpan data user

if "user_data" not in st.session_state:

    st.session_state.user_data = {

        "budget": 0,

        "ingredients": [],

        "estimated_cost": 0

    }



# menyimpan mode

if "mode" not in st.session_state:

    st.session_state.mode = "Normal"



# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:


    st.header("⚙️ Pengaturan")


    # ======================
    # PILIH MODE
    # ======================

    st.subheader("🎯 Mode Masak")


    selected_mode = st.selectbox(

        "Pilih kondisi kamu",

        [

            "Normal",

            "Quick Cooking",

            "Akhir Bulan Survival",

            "Anti Mubazir"

        ]

    )


    st.session_state.mode = selected_mode



    st.divider()



    # ======================
    # BUDGET
    # ======================

    st.subheader("💰 Budget")


    budget = st.number_input(

        "Masukkan budget makan",

        min_value=0,

        value=st.session_state.user_data["budget"],

        step=1000

    )


    st.session_state.user_data["budget"] = budget



    if budget > 0:


        st.success(

            f"Rp{budget:,}"

        )

    else:

        st.info(
            "Budget belum diatur"
        )



    st.divider()



    # ======================
    # BAHAN TERDETEKSI
    # ======================

    st.subheader("🥬 Bahan Terdeteksi")



    ingredients = st.session_state.user_data["ingredients"]



    if ingredients:


        for item in ingredients:


            st.write(

                f"• {item}"

            )


    else:


        st.caption(

            "Belum ada bahan"

        )



    st.divider()



    # ======================
    # ESTIMASI BIAYA
    # ======================


    st.subheader("🧾 Estimasi Bahan")



    cost = st.session_state.user_data.get(

        "estimated_cost",

        0

    )


    if cost > 0:


        st.success(

            f"Rp{cost:,}"

        )


    else:


        st.caption(

            "Belum dihitung"

        )



    st.divider()



    # ======================
    # CONTOH PROMPT
    # ======================


    st.subheader("💡 Contoh Input")


    st.write(

        """
• Saya punya telur dan nasi

• Budget saya 10000

• Saya punya kentang wortel

• Saya mau menu akhir bulan

"""

    )



    st.divider()



    # ======================
    # RESET
    # ======================


    if st.button(

        "🔄 Reset Chat",

        use_container_width=True

    ):


        reset_history()


        st.session_state.messages = []


        st.session_state.user_data = {

            "budget":0,

            "ingredients":[],

            "estimated_cost":0

        }


        st.rerun()



# ==========================================
# MENAMPILKAN HISTORY CHAT
# ==========================================


for message in st.session_state.messages:


    with st.chat_message(

        message["role"]

    ):


        st.markdown(

            message["content"]

        )



# ==========================================
# INPUT USER
# ==========================================


user_input = st.chat_input(

    "Contoh: Saya punya telur, nasi, dan sawi"

)



if user_input:



    # simpan pesan user

    st.session_state.messages.append(

        {

            "role":"user",

            "content":user_input

        }

    )



    with st.chat_message("user"):


        st.markdown(

            user_input

        )



    # ===============================
    # STREAM RESPONSE AI
    # ===============================


    with st.chat_message("assistant"):


        response = st.write_stream(

            chat_stream(

                user_input,

                st.session_state.user_data,

                st.session_state.mode

            )

        )



    # simpan jawaban AI

    st.session_state.messages.append(

        {

            "role":"assistant",

            "content":response

        }

    )



    # refresh sidebar

    st.rerun()