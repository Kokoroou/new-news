import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader


def hash_password(plain_password: str = "") -> str:
    hashed_password = stauth.Hasher([plain_password]).generate()[0]
    print(hashed_password)

    return hashed_password


def _load_config():
    with open('../../config/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    return authenticator


def login(authenticator):
    """Show login widget"""
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')


def register(authenticator):
    """Show register widget"""
    pass


def run():
    st.markdown('<h1 style="text-align: center;">New news</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center;">Explore new amazing news for you.</h2>', unsafe_allow_html=True)

    authenticator = _load_config()
    login(authenticator)


run()


# if __name__ == '__main__':
#     hash_password('123456')
