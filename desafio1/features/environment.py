from features.utils.config import URL_AMBIENTE
from features.utils.util import Util
from behave.log_capture import capture
from features.utils.web_app import webapp


def before_scenario(context, scenario):
    webapp.go_site(URL_AMBIENTE)


@capture()
def after_step(context, step):
    util = Util()
    if step.status == 'failed':
        nome_final = util.limpa_nome_step(step)
        context.driver.save_screenshot('features/report/erro' + nome_final + '.png')