# Traduções PT-BR de mods do RimWorld

Traduções de interface de mods do RimWorld, preparadas para instalação por cópia na pasta da Oficina Steam. O [release mais recente](https://github.com/Kyo-70/RimWorld-Mods_PT-BR/releases/latest) contém um ZIP com as pastas identificadas pelo ID de cada item da Oficina.

## Mods disponíveis

| Mod | Versão de referência | Oficina Steam | Tradução |
| --- | --- | --- | --- |
| [Pawn Editor Forked](https://github.com/segaswolf/pawn-editor-forked) | 3.2.4, commit `986a7c7714e11cdfa80473e70f7d72d37cf6f816` | [3667931113](https://steamcommunity.com/sharedfiles/filedetails/?id=3667931113) | 456 de 456 chaves nos arquivos `Settings.xml` e `UI.xml` |

## Instalar pela Oficina Steam

1. Inscreva-se no [Pawn Editor Forked](https://steamcommunity.com/sharedfiles/filedetails/?id=3667931113) e no [Harmony](https://steamcommunity.com/sharedfiles/filedetails/?id=2009463077). Abra o jogo uma vez para baixar os mods. Ative o Pawn Editor Forked depois do Harmony e selecione **Português (Brasil)** como idioma do RimWorld.
2. Baixe o arquivo `RimWorld_Mods_PT-BR_v1.0.0.zip` na página de [releases](https://github.com/Kyo-70/RimWorld-Mods_PT-BR/releases).
3. Abra a pasta da biblioteca Steam que contém o RimWorld. Em uma instalação padrão no Windows, o destino é `C:\Program Files (x86)\Steam\steamapps\workshop\content\294100\`. Se o jogo estiver em outra unidade ou biblioteca, use a pasta `steamapps\workshop\content\294100\` dessa biblioteca.
4. Extraia o ZIP. **Copie a pasta `3667931113` de dentro dele para `294100`**, confirmando a mesclagem das pastas. O destino final deve ser `...\294100\3667931113\Languages\PortugueseBrazilian\Keyed\UI.xml`, com `Settings.xml` ao lado.
5. Reinicie o RimWorld. Se a Steam atualizar o mod e remover a tradução, repita a cópia do ZIP.

No Linux, o caminho costuma ser `~/.local/share/Steam/steamapps/workshop/content/294100/`. A pasta `3667931113` já precisa conter o mod baixado pela Steam: o ZIP fornece apenas a tradução.

## Organização

```text
mods/
  PawnEditorForked/
    Languages/PortugueseBrazilian/Keyed/
      Settings.xml
      UI.xml
mods.json
scripts/build_release.py
scripts/validate_translation.py
```

Para incluir outro mod, siga [COMO_ADICIONAR_MOD.md](COMO_ADICIONAR_MOD.md). O comando `python scripts/build_release.py --version v1.0.0` gera um ZIP com todos os mods cadastrados em `mods.json`, cada um na pasta de seu ID da Oficina.

## Créditos e escopo

O mod [Pawn Editor Forked](https://github.com/segaswolf/pawn-editor-forked) é mantido por Segas Wolf e credita ISOR3X, legodude17 e demais colaboradores. Este repositório publica somente textos de tradução; não distribui DLLs, imagens nem os outros arquivos do mod. A tradução é independente e não é uma publicação oficial dos autores do mod. O código original não apresenta licença explícita no README consultado; consulte os autores antes de redistribuí-lo.
