import importlib

import click

import framework.logger
import framework.notification.crash_push_service
from framework.config import BasicConfig
from framework.package_tools.path_utils import path_to_package

logger = framework.logger.getLogger(__name__)
sendkey = 'replace with your token'


@click.command()
@click.option('--script', default='')
@click.option('--config', default='exp_unet_casia2/configs/unet2d_casia2_stage2_448_resize_224_relation_evaluate.py')
@click.option('--gpu', default='0')
@click.option('--push_message', default=False)
def boot(script: str, config: str, gpu: str, push_message: bool):
    """
    启动入口，运行script，把config传给它。
    :param script: exp_multi_points.unet_split_rgb_casia2_multi_point_400_input_relation_evaluate
    :param config: 例如 exp_test.print_config
    :param gpu: 快速覆盖gpu的设置
    :param push_message: 是否推送崩溃消息
    """
    if push_message:
        logger.info('push service on crash: ON!')
    if '/' in config or config.endswith('.py'):
        config = path_to_package(config)
    if '/' in script or script.endswith('.py'):
        script = path_to_package(script)
    config_mod = importlib.import_module(config)
    assert hasattr(config_mod, 'get_config'), logger.error(f'no module {config}')
    config = config_mod.get_config()
    assert isinstance(config, BasicConfig)

    if gpu:
        config.gpu = gpu
    config.build()

    if not script:
        script = config.script

    script_mod = importlib.import_module(script)
    assert hasattr(script_mod, 'main'), logger.error(f'no module {script}')
    try:
        script_mod.main(config)
    except Exception as e:
        if push_message:
            framework.notification.crash_push_service.push(
                title=f'Crash on running task {script}',
                message=e,
                push_service_token=sendkey,
            )


if __name__ == '__main__':
    boot()
