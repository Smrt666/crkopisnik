import sys

def main(zoom_mode=False, viber_mode=False, fill=False):
        besedilo = input('Napiši besedilo: ')
        besedilo = list(besedilo.casefold())

        viber_replace = '"' #'¨' - blizu #chr(9617)  # '.'  # chr(9617)

        crke = dict()
        for crka in 'abcčdefghijklmnoprsštuvzž':
                with open('crke\\'+crka+'.txt', 'r', encoding='utf-8') as f:
                        if viber_mode and fill:
                                x = f.read()
                                x = x.split('\n')
                                x = [i + viber_replace*(10-len(i)) for i in x]
                                crke[crka] = '\n'.join(x)
                                # najdaljša vrstica je 10
                        else:
                                crke[crka] = f.read()
        output = '\n'
        for crka in besedilo:
                nova = crke.get(crka, None)
                if nova is None:
                        if crka == ' ':
                                output += '\n'*5
                else:
                        output += nova + '\n'

        if zoom_mode:
                output = output.replace(' ', chr(8194))
        elif viber_mode:
                output = output.replace(' ', viber_replace)


        print(output)

if __name__ == '__main__':
        kwgs = {}
        kwgs['zoom_mode'] = 'zoom_mode' in sys.argv
        kwgs['viber_mode'] = 'viber_mode' in sys.argv
        kwgs['fill'] = '-fill' in sys.argv
        
        main(**kwgs)
