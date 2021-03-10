from framework.config.basic import BasicConfig
from framework.logger import getLogger

logger = getLogger(__name__)

class Config(BasicConfig):

    def __init__(self) -> None:
        super().__init__()
        self.save_path = 'save/example_test'
        # 注册路径会被框架自动创建
        self.register_path(self.save_path)
        self.visdom_env = 'liupeng_' + 'unet3d_224_input'
        self.batch_size = 2
        self.val_batch_size = 2
        self.input_size = 224
        self.script = 'exp_test/print_config.py'
        self.gpu = '5,7'
        self.sigma = 5


    def build(self):
        super().build()
        # 可以在这里做一些额外的信息输出
        logger.info(f'sigma: {self.sigma}')


def get_config():
    """
    返回的配置必须是`framework.config.BasicConfig`的实例，函数名字必须为`get_config`。
    """
    return Config()
