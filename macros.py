import requests


def define_env(env):
    def get_markdown(url):
        response = requests.get(url)
        return response.content.decode()
    env.macro(get_markdown, 'get_markdown')