import streamlit as st
import subprocess


def main():
    subprocess.run(["crewai", "run"])

    with open("report.md", "r", encoding="utf-8") as src:
        st.write(src.read())


if __name__ == "__main__":
    main()
