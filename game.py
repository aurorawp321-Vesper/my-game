import streamlit as st
import random

st.set_page_config(page_title="猜数字游戏", page_icon="🎮")

st.title("🎮 猜数字游戏")

# 初始化游戏状态
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

if not st.session_state.game_over:
    guess = st.number_input("请输入你的猜测 (1-100):", min_value=1, max_value=100, step=1)

    if st.button("猜测!"):
        st.session_state.attempts += 1

        if guess < st.session_state.target:
            st.warning(f"🔼 再大一点！已猜 {st.session_state.attempts} 次")
        elif guess > st.session_state.target:
            st.warning(f"🔽 再小一点！已猜 {st.session_state.attempts} 次")
        else:
            st.session_state.game_over = True
            st.balloons()
            st.success(f"🎉 恭喜猜对！答案是 {st.session_state.target}")
            st.info(f"共猜了 {st.session_state.attempts} 次")
else:
    st.success(f"答案是 **{st.session_state.target}**，用了 **{st.session_state.attempts}** 次！")

if st.button("🔄 重新开始"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()