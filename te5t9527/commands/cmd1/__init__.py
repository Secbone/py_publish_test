import sys
import argparse

def func(args):
    """detect csv data
    """

    sys.stdout.write('reading data....\n')
    with args.input as input:
        data = pd.read_csv(input)

    sys.stdout.write('detecting...\n')
    report = data

    if args.output:
        sys.stdout.write('saving report...\n')
        report.to_csv(args.output)
        sys.stdout.write('report saved!\n')
    else:
        sys.stdout.write(str(report))
        sys.stdout.write('\n')

    return report

ARGS = {
    'info': {
        'name': 'detect',
        'description': 'detect data from a csv file',
    },
    'defaults': {
        'func': func,
    },
    'args': [
        {
            'flag': ('-i', '--input'),
            'type': argparse.FileType(),
            'help': 'the csv file which will be detected',
            'required': True,
        },
        {
            'flag': ('-o', '--output'),
            'type': argparse.FileType('w'),
            'help': 'path of the csv report will be saved',
        },
    ]
}
