from pathlib import Path
import os
import framework.logger
from framework.package_tools.path_utils import path_to_package

logger = framework.logger.getLogger(__name__)


class BasicConfig:
    """
    所有的新实验设置都必须创建一个新的`BasicConfig`实例，然后进行增删。
    """
    save_path: str
    script: str
    gpu: str

    def __init__(self) -> None:
        self.gpu = '0, 1'
        self.batch_size = 4
        self.save_path = 'save'
        self.visdom_env = 'liupeng_test1'
        self.epoch = 1000
        self.lr = 1e-4
        self.num_workers = 4
        self.input_size = 400
        self.val_batch_size = 1
        self.val_num_workers = 2
        self.script = ''
        self.path_to_init = []
        self.evaluate = False

    def build(self):
        self.init_path()
        self.path_to_package()
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = self.gpu
        logger.info('------experiment overview------')
        logger.info(f'script name: {self.script}')
        logger.info(f'save_path: {self.save_path}')
        logger.info(f'visdom_env: {self.visdom_env}')
        logger.info(f'input size: {self.input_size}')
        logger.info(f'batch size: {self.batch_size}')
        logger.info(f'gpu use: {self.gpu}')

    def merge_yaml(self, yaml_file):
        """
        今后有空会实现`.yaml`配置，目前暂不做。
        :param yaml_file: yaml的路径
        :return: 合并后的`BasicConfig`实例
        """
        return self

    def path_to_package(self):
        if '/' in self.script or self.script.endswith('.py'):
            self.script = path_to_package(self.script)

    def init_path(self):
        for path in self.path_to_init:
            if not os.path.exists(path):
                os.makedirs(path)

    def register_path(self, path):
        self.path_to_init.append(path)
