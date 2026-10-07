<!-- LOVABLE:BEGIN -->
> [!IMPORTANT]
> This project is connected to [Lovable](https://lovable.dev). Avoid rewriting
> published git history — force pushing, or rebasing/amending/squashing commits
> that are already pushed — as it rewrites history on Lovable's side and the
> user will likely lose their project history.
>
> Commits you push to the connected branch sync back to Lovable and show up in
> the editor, so keep the branch in a working state.
<!-- LOVABLE:END -->

- Edit the so_shop catalog only in `tools/build_so_shop_catalog.py` and regenerate; it owns item/, menu/, dialog/ and the dispatchers while hand-verified lib (progress, cooldown, sell limit) stays untouched, so one source avoids drift between chat and dialog menus.
- Lock so_shop articles per item (block-count guard in each buy function and detail opener), never per section; players need early access to cosmetic items in every section.
- Keep Simply OneBlock keys as vanilla trial keys with the exact plain `minecraft:custom_name` strings shared with `so_crates`; their original chamber doors and crate vaults depend on exact matching.
- Build `so_quests` state-aware UI as dynamic inline dialogs (macro'd `$dialog show` fed from `storage so_quests:menu` in `function/menu/cat_*`), not static dialog JSON; per-player button colors cannot be expressed in static dialog files.
