from src.utils.pipeline import Pipeline
from src.utils.enums import Source


def main():
    list_of_sources = [Source.FN9, Source.MGP, Source.RCR]

    for source in list_of_sources:
        pipeline = Pipeline(source)
        pipeline.write_source_yml()
        pipeline.write_models()
        pipeline.write_gold_models()


if __name__ == "__main__":
    main()
