import os
import fnmatch
import sys

print('-'*50)
print("Sistema: ",sys.platform)

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\bin\ffmpeg.exe'

codec_video = '-c:v libx264'
codec_audio = '-c:a aac'

crf = '-crf 20'

preset = '-preset ultrafast'

bitrate_audio = '-b:a 320k'

debug = ''

caminho_origem = '.\Videos'
caminho_destino = '.\Saida'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)

        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho, legenda = os.path.splitext(nome_arquivo)
        print('caminho: ',caminho)
        print('legenda: ',legenda)
        caminho_legenda = nome_arquivo + '.srt'
        print('caminho_legenda: ',caminho_legenda)
        print('nome_arquivo: ',nome_arquivo)
        print('')        

        if os.path.isfile(caminho_legenda):
    
            input_legenda = caminho_legenda
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:

            input_legenda = ''
            map_legenda = ''
            
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        extensao_arquivo = 'mkv'

        nome_novo_arquivo = nome_arquivo + '_NOVO.' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)
        
        comando = f'{comando_ffmpeg} -i "{caminho_completo}" -i {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} {map_legenda} "{arquivo_saida}"'
        print('raiz: ',raiz)
        print('nome_novo_arquivo: ',nome_novo_arquivo)
        print(f'comando_ffmpeg: {comando_ffmpeg}\n"caminho_completo: {caminho_completo}"\ninput_legenda: {input_legenda}\ncodec_video: {codec_video}\ncrf: {crf}\npreset: {preset}\ncodec_audio: {codec_audio}\nbitrate_audio: {bitrate_audio}\ndebug: {debug}\nmap_legenda: {map_legenda}\narquivo_saida: "{arquivo_saida}"')

        print('-'*100)
        print('\n')
        print(comando)
        print('\n')
        print('-'*100)
        print('\n')
        os.system(comando)

        input("Arquivo Convertido - Tecle [ ENTER ]")
        
