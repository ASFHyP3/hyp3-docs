import requests


def define_env(env):
    def get_content(url):
        response = requests.get(url)
        return response.content.decode()
    env.macro(get_content, 'get_markdown')