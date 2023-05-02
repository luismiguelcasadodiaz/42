#!/usr/bin/python3

import os
import sys

def create_argument_parser():

    def uniform_resource_locator(url_txt):
        """
          helper function that validates url passed at command line
        """
        # 1.- urlparse splits componenst
        parsed_url = urlparse(url_txt)
        # 2.- check if scheme is allowed in this app
        if parsed_url.scheme in ALLOWED_SCHEMES:
            if parsed_url.scheme in WEB_SCHEMES:
                # validators does not accept other schemes than http
                fake_url = "https://" + parsed_url.netloc
                # 3.- check if netloc/domain/autohity i ok
                ok_url = validators.url(fake_url)
                if not ok_url:
                    parser.error(f"Invalid WEB url {url_txt}")
                else:
                    # 4.- returns ALLOWED SCHEME and valid Authuority
                    return url_txt
            else:
                # we face a file path
                if os.path.isfile(parsed_url.path):
                    return url_txt
                else:
                    parser.error(f"Invalid PATH {url_txt}")

        else:
            # passed scheme is not allowed
            problem1 = parsed_url.scheme
            msg = f"Scheme '{problem1}' from url {url_txt} not allowed"
            parser.error(msg)

    def correct_filename(argument):
        """
          helper function that recursion level passed at command line
        """
        if argument is None:
            parser.error(f"Missing file name '{argument}'")
        else:
            try:
                cwd = os.getcwd()
                filepath = os.path.join(cwd, argument)
                if os.path.isfile(filepath):
                    if not os.access(spiderpath, os.R_OK):
                        parser.error(f"can not read'{argument}'")
            except:
                parser.error(f"Incorrect recursivity level '{argument}'")
    msg = """
    Permet d’enregistrer un mot de passe initial, et qui est capable"
    de générer un nouveau mot de passe chaque fois qu’il est demandé"""
    parser = argparse.ArgumentParser(
                                     prog='Time One-Time-Password generator',
                                     description=msg,
                                     epilog='Este es el final de la ayuda')

    parser.add_argument('-g',
                        help='Clave hexadecimal de mas de 64 caracters',
                        action='store_true',
                        default=False
                        )

    parser.add_argument( '-k',
                        help=f'I need a file ft_otp.key, qui sera crypté.',
                        type=correct_filename)


    return parser


if __name__ == "__name__":
    parser = create_argument_parser()
    pprint(sys.argv)
    args = parser.parse_args(sys.argv[1:])