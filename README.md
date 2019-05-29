# gen-title-info-entry

Experimental script to generate the [Title Info Entry](https://www.3dbrew.org/wiki/Title_Database#Title_Info_Entry) for `title.db`.

Example for 0004000000164800 Pokémon Sun:
```
python3 gen-title-info-entry.py \
        --version 32 \
        --has-manual \
        --tmd-id 0 \
        --cmd-id 1 \
        --has-save \
        --extdata-id 1648 \
        --product-code CTR-P-BNDA \
        -o /path/to/titledb/mount/0004000000164800
```

License: MIT
