from dataclasses import dataclass, asdict

from asyncpg.pgproto.pgproto import UUID


def list_response(items):
    res = []
    for i in items:
        item = asdict(i)
        for k, _ in item.items():
            if isinstance(item[k], UUID):
                item[k] = str(item[k])
        res.append(item)
    
    return {"items": res}