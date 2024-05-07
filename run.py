import argparse
from lib.predict_multi_batch import cal_musit

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='MusiteDeep prediction tool for general, kinase-specific phosphorylation prediction or custom PTM prediction by using custom models.')
    parser.add_argument('-input',  dest='inputfile', type=str, help='Protein sequences to be predicted in FASTA format.', required=True)
    parser.add_argument('-output',  dest='output', type=str, help='prefix of the prediction results.', required=True)
    parser.add_argument('-model-prefix',  dest='modelprefix', type=str, help='prefix of custom model used for prediciton. If donnot have one, please run train_capsnet_10fold_ensemble.py and train_CNN_10fold_ensemble to train models for a particular PTM type.', required=False,default=None)
    args = parser.parse_args()

    success = cal_musit(args.inputfile, args.output, args.modelprefix)
    if success:
        print('Operation completed successfull')

# python run.py -input [custom prediction data in FASTA format] -output [custom specified prefix for the prediction results] -model-prefix [prefix of pre-trained model]
# python run.py -input example/input/seq.fasta -output example/output/result -model-prefix models/N-linked_glycosylation
# python run.py -input example/input/seq.fasta -output example/output/result -model-prefix "models/Phosphotyrosine;models/Methyllysine"