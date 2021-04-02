import requests


def define_env(env):
    def get_content(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content.decode()
    env.macro(get_content, 'get_markdown')