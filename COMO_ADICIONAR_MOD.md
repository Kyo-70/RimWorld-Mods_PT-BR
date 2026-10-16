# Como adicionar outro mod

1. Verifique o repositório e a página da Oficina do mod. Anote o ID numérico da Oficina e a versão ou commit usado como referência.
2. Crie `mods/NomeDoMod/Languages/PortugueseBrazilian/Keyed/`. Para textos de definições, use também `DefInjected/` conforme a estrutura do mod. Coloque nessa pasta apenas os arquivos de idioma que você traduziu. Mantenha as tags XML, marcadores como `{0}`, quebras `\n` e IDs de definições; traduza apenas o texto apresentado ao jogador.
3. Cadastre o mod em `mods.json` com `slug`, `workshopId`, `name`, `sourceUrl` e `sourceVersion`. Cada ID da Oficina deve ser exclusivo.
4. Execute `python scripts/build_release.py --version v1.1.0`. O script valida XML, identifica chaves duplicadas e cria `dist/RimWorld_Mods_PT-BR_v1.1.0.zip` com uma pasta de ID da Oficina para cada mod.
5. Se você tiver os arquivos originais de idioma, compare as chaves e os marcadores com `python scripts/validate_translation.py --mod NomeDoMod --source /caminho/para/o/mod`. Corrija qualquer chave ou marcador ausente antes de publicar.
6. Atualize a tabela do `README.md` e as instruções do release.

O arquivo ZIP foi pensado para mesclar com mods já instalados pela Steam. Não inclua executáveis, DLLs, texturas, arquivos de origem alheios ou o mod completo sem permissão dos autores.
