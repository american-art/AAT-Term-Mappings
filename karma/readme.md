# AAT Term

Source data requirement:

- format in csv.
- has header
- column A is classification term, column B is AAT term, column C is AAT URI.
- file name start with museum name abbreviation and a space.

This script will generate following dictionary in python.

    {
        museum: {
            classification term: {
                "aat_term": string,
                "aat_uri": string
            }
            ...
        }
        ...
    }

Copy generated script file to KARMA_HOME/python.

API:

    AATTerm.get_aat_uri(museum, classification_term)
    AATTerm.get_aat_term(museum, classification_term)


