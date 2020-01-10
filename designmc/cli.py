import argparse
import textwrap
import os
import pandas as pd
from glob import glob
from reframed import Environment, ModelCache
from .designmc import design


def main():
    parser = argparse.ArgumentParser(description="Design microbial communities.")

    parser.add_argument('models', metavar='MODELS', nargs='+',
                    help=textwrap.dedent(
    """
    Multiple single-species models (one or more files).
    
    You can use wild-cards, for example: models/*.xml, and optionally protect with quotes to avoid automatic bash
    expansion (this will be faster for long lists): "models/*.xml". 
    """
    ))

    parser.add_argument('-t', '--target', dest="target",required=True, help="Target compound to maximize (example: etoh, succ, trp__L).")

    parser.add_argument('-s', '--species', dest="species", type=int, default=1, help="Maximum number of species (default: 1).")
    parser.add_argument('-n', '--iters', dest="iters", type=int, default=100, help="Maximum number of iterations (default: 100).")
    parser.add_argument('-g', '--growth', dest="growth", type=float, default=0.1, help="Target community growth rate (default: 0.1 h-1).")

    parser.add_argument('-m', '--media', dest="media", required=True, help="Run for given media (comma-separated).")
    parser.add_argument('-d', '--mediadb', dest="mediadb", required=True, help="Media database file")

    parser.add_argument('-o', '--output', dest="output", default='out.tsv', help="Output filename.")

    args = parser.parse_args()

    ## load models

    models = args.models
    if len(models) == 1 and '*' in models[0]:
        models = glob(models[0])
        if len(models) == 0:
            raise IOError(f"No files found: {models}.")

    species = [extract_id_from_filepath(model) for model in models]
    cache = ModelCache(species, models)

    ## load media

    try:
        mediadb = load_media_db(args.mediadb)
    except:
        raise IOError(f"Unable to load media db file: {args.mediadb}.")

    media = args.media.split(",")

    dfs = []

    target = f"R_EX_M_{args.target}_e"

    for medium in media:
        if medium not in mediadb:
            raise RuntimeError(f"Medium {medium} not in database.")

        print(f"Optimizing {args.target} production in medium {medium}.")

        env = Environment.from_compounds(mediadb[medium], fmt_func=lambda x: f"R_EX_M_{x}_e")
        df = design(species, target, env, size=args.species, iters=args.iters, growth=args.growth, modelcache=cache)
        df["medium"] = medium
        df["target"] = args.target
        dfs.append(df)

    dfs = pd.concat(dfs)
    dfs = dfs[["medium", "initial", "stable", "species", "target", "value"]]

    dfs.to_csv(args.output, sep="\t", index=False)



def load_media_db(filename, sep='\t', medium_col='medium', compound_col='compound'):
    """ Load media library file. """

    data = pd.read_csv(filename, sep=sep)
    media_db = data[[medium_col, compound_col]].groupby(medium_col).agg(lambda x: list(x))

    return media_db[compound_col].to_dict()


def extract_id_from_filepath(filepath):
    filename = os.path.basename(filepath)

    if filename.endswith('.xml'):
        organism_id = filename[:-4]
    elif filename.endswith('.xml.gz'):
        organism_id = filename[:-7]
    else:
        raise IOError(f"Unrecognized extension in file {filename}. Valid extensions are .xml and .xml.gz")

    return organism_id


if __name__ == "__main__":
    main()
