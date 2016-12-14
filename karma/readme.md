# AAT Term

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


