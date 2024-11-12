import datetime as dt


def parse_timestamp(timestamp: str | int | float) -> str:
    match timestamp:
        case int() | float():
            timestamp_in_seconds = timestamp / 1000 if timestamp > 10**10 else timestamp
            datet = dt.datetime.fromtimestamp(timestamp_in_seconds, tz=dt.timezone.utc)
        case str():
            try:
                datet = dt.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            except ValueError:
                n_timest = float(timestamp)
                timest_in_s = n_timest / 1000 if n_timest > 10**10 else n_timest
                datet = dt.datetime.fromtimestamp(timest_in_s, tz=dt.timezone.utc)
        case _:
            raise ValueError(f"Unsupported timestamp format {type(timestamp)}")

    return datet.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
