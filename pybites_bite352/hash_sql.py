import hashlib
from random import shuffle

query = """select Candidate, Election_year, sum(Total_$), count(*)
    from combined_party_data
    where Election_year = 2016
    group by Candidate, Election_year
    having count(*) > 80
    order by count(*) DESC;
    """


def hash_query(query: str, length: int = 32) -> str:
    """Return a hash value for a given query.

    Args:
        query (str): An SQL query.
        length (int, optional): Length of the hash value. Defaults to 32.

    Raises:
        ValueError: Parameter length has to be greater equal 1.
        TypeError: Parameter length has to be of type integer.

    Returns:
        str: String representation of the hashed value.
    """

    if length < 1:
        raise (ValueError)

    if not isinstance(length, int):
        raise (TypeError)

    query = query.replace(";", "")
    query = query.strip()
    query = query.lower()
    query = query.replace('"', "")

    query_split = query.split()
    query_split.sort()
    query_split = " ".join(query_split)

    query_bytes = str.encode(query_split)
    sha512 = hashlib.sha512()
    sha512.update(query_bytes)
    query_hash = sha512.hexdigest()

    return query_hash[:length]
