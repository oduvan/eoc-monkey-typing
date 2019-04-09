"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['How aresjfhdskfhskd you?', ['how', 'are', 'you', 'hello']],
            "answer": 3,
            "show": "'How aresjfhdskfhskd you?', {'you', 'how', 'hello', 'are'}",
            "explanation": '<strong>How</strong> <strong>are</strong>sjfhdskfhskd <strong>you</strong>?'
        },
        {
            "input": ['Bananas, give me bananas!!!', ['banana', 'bananas']],
            "answer": 2,
            "show": "'Bananas, give me bananas!!!', {'banana', 'bananas'}",
            "explanation": '<strong>Bananas</strong>, give me <strong>bananas</strong>!!!'
        },
        {
            "input": ['Lorem ipsum dolor sit amet, consectetuer adipiscing elit.',
                      ['sum', 'hamlet', 'infinity', 'anything']],
            "answer": 1,
            "show": "'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', {'hamlet', 'sum', 'infinity', 'anything'}",
            "explanation": 'Lorem ip<strong>sum</strong> dolor sit amet, consectetuer adipiscing elit.'
        },
    ],
    "Edge": [
        {
            "input": ['A', ['the']],
            "answer": 0,
            "show": "A, {'the'}",
            "explanation": 'A'
        },
        {
            "input": [
                'PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXmgatDzedINMmRVxWCIeUfXShDvlWCQtgGYXOxsFpdlNHhxUBRAwAZqXdCkFdjYhBGwpVwJngGxgTDdBHVDdufWGbdENvxbOMylqdPWBiKpptHbXuZwFKBAwCGiXNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJjdeTSHuhJRvUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUhm',
                ['the', 'who', 'any', 'man', 'hey', 'box', 'zed']],
            "answer": 1,
            "show": "'PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXmgatDzedINMmRVxWCIeUfXShDvlWCQtgGYXOxsFpdlNHhxUBRAwAZqXdCkFdjYhBGwpVwJngGxgTDdBHVDdufWGbdENvxbOMylqdPWBiKpptHbXuZwFKBAwCGiXNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJjdeTSHuhJRvUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUhm', {'man', 'who', 'the', 'any', 'zed', 'hey', 'box'}",
            "explanation": 'PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXmgatD<strong>zed</strong>INMmRVxWCIeUfXShDvlWCQtgGYXOxsFpdlNHhxUBRAwAZqXdCkFdjYhBGwpVwJngGxgTDdBHVDdufWGbdENvxbOMylqdPWBiKpptHbXuZwFKBAwCGiXNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJjdeTSHuhJRvUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUhm'
        },

    ],
    "Extra": [
        {
            "input": ['LOLOLOLOLOL', ['lol', 'olo']],
            "answer": 2,
            "show": "'LOLOLOLOLOL', {'lol', 'olo'}",
            "explanation": '<strong>LOLOLOLOLOL</strong>'
        },
        {
            "input": ['ab cd', ['abc']],
            "answer": 0,
            "show": "'ab cd', {'abc'}",
            "explanation": 'ab cd'
        },
        {
            "input": ['Oooooooooooo Thhhhe', ['the', 'hey']],
            "answer": 0,
            "show": "'Oooooooooooo Thhhhe', {'hey', 'the'}",
            "explanation": 'Oooooooooooo Thhhhe'
        },
        {
            "input": [
                'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
                ['far', 'word', 'vokal', 'count', 'tries']],
            "answer": 5,
            "show": "'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.', {'far', 'word', 'count', 'vokal', 'tries'}",
            "explanation": '<strong>Far</strong> <strong>far</strong> away, behind the <strong>word</strong> mountains, <strong>far</strong> from the <strong>countries</strong> <strong>Vokal</strong>ia and Consonantia, there live the blind texts.'
        },
        {
            "input": [
                'The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps.',
                ['nobody', 'hamlet', 'sophia', 'nikola', 'stephan']],
            "answer": 0,
            "show": "'The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps.', {'nobody', 'sophia', 'nikola', 'hamlet', 'stephan'}",
            "explanation": 'The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps.'
        },
        {
            "input": [
                'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born',
                ['this', 'that', 'they', 'she', 'hello', 'world']],
            "answer": 1,
            "show": "'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born', {'this', 'world', 'she', 'hello', 'they', 'that'}",
            "explanation": 'But I must explain to you how all <strong>this</strong> mistaken idea of denouncing pleasure and praising pain was born'
        },
    ]
}
