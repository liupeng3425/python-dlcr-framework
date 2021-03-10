from exp_test.configs.example_push_service import Config
from framework.logger import getLogger

logger = getLogger(__name__)


def train(network, batch_size, gpu):
    logger.info(f'train {network} completed, batchsize={batch_size}, gpu={gpu}')


def main(config: Config):
    logger.info('running task')
    # 运行示例网络训练
    train('resnet', config.batch_size, config.gpu)
    if config.raise_error_test:
        a = 1 / 0
    logger.info('task complete!')
