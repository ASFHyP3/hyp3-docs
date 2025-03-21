import requests

_CREDITS_PER_MONTH_VALUE = 10_000
CREDITS_PER_MONTH = f'{_CREDITS_PER_MONTH_VALUE:,}'


def define_env(env):
    env.macro(CREDITS_PER_MONTH, 'CREDITS_PER_MONTH')

    def get_content(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content.decode()

    env.macro(get_content, 'get_content')

    def table_indent(count=1):
        return '&nbsp;' * count * 8

    env.macro(table_indent, 'table_indent')

    def max_jobs_per_month(credit_cost):
        return f'{_CREDITS_PER_MONTH_VALUE // credit_cost:,}'

    env.macro(max_jobs_per_month, 'max_jobs_per_month')
