# tfRec: An open source toolkit for Recommender Systems by tensorflow
This repository provides a standard RS(Recommender Systems）training and testing framework. In this framework, we implement typical RS models under this framework based on tensorflow, which enables these models to be trained with GPUs.

The implemented or modified models include SVD, BMF, SVD++, MSVD, CIC and CFM.
# Quickstart
- Clone this repo.
- enter the directory where you clone it, and run the following code
    ```bash
    pip install -r requirements.txt
    python tfRec --method SVD
    ```
## Options
You can check out the other options available to use with *OpenNE* using:

    python -m tfRec --help

- -d, --dataset, The dataset name; the default is ta;
- --K, Number of latent vectors; the default is 50;
- --criteriaNum, Number of criteria ratings; the default is 6;
- --cv, ,The cv in datasets; the default is 10;
- --percent, The percent in trainning; the default is 02;
- -e, --epochs, The training epochs; the default is 1;
- --batchSize, The batch size of training; the default is 1;
- --lr, The learning rate; the default is 0.1;
- --learner, the optimazation algorithms; the default is adam;
- --maxR, The maximum rating of datasets; the default is 5.0;
- --minR, The minimum rating of datasets; the default is 1.0;
- --method, The learning method (SVD,SVDPP, BMF, CIC, CFM); 
- --biasR, The regularization of biasd in BMF et. al; the default is 0.01;
- --uR, The regularization of users\ latent vector; the default is 0.01;
- --iR, The regularization of items\ latent vector; the default is 0.01;
- --regressionR, The regularization of regression weights; the default is 0.01;
- --criR, The regularization of criteria weights for MSVD; the default is 0.01;
- --reg, set regularization for all weights (for SVDPP); the default is 0.01;
- --lam, The effect of criteria rating in CFM et. al; the default is 0.01;
- --share, sharing users' or items' for CFM model (user ,item ,ind); the default is ind;
- --saveThreshold, The Threshold for saving model,the default is 0.89;
- --CPU, The numbers of CPU cores, the default is 1;
- --GPU, The numbers of GPU cores, the default is 0;


# Author
[Ge Fan](http://fange.ml/), [simileLab](http://smilelab.uestc.edu.cn/) (fange@std.uestc.edu.cn)

## Citing
If you find *tfRec* is useful for your research, please consider citing the following papers:

        @article{chen2017preference,
        title={Preference modeling by exploiting latent components of ratings},
        author={Chen, Junhua and Zeng, Wei and Shao, Junming and Fan, Ge},
        journal={Knowledge and Information Systems},
        pages={1--27},
        year={2017},
        publisher={Springer}
        }

        @inproceedings{paterek_2007_KDDcup,
        title={Improving regularized singular value decomposition for collaborative filtering},
        author={Paterek, Arkadiusz},
        booktitle={Proceedings of KDD cup and workshop},
        volume={2007},
        pages={5--8},
        year={2007}
        }
        