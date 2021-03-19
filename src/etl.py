from src.extract import extract
from src.load import load
from src.transform import transform



def pipe(event, context):
    print(event)
    raw = extract(event)
    print(raw)
    transformed = transform(raw.values.tolist())
    print(transformed)
    load(transformed)


pipe(None, None)