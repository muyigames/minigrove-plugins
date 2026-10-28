# Native Codex CLI evidence walkthrough

[Play the edited walkthrough](assets/minigrove-native-codex-walkthrough.mp4) · [Actual selected tool events and source hashes](assets/native-walkthrough-evidence.json)

178 seconds, 1920×1080 H.264 MP4. Recorded native client: Codex CLI 0.156.1, gpt-6-luna, fresh company account sign-in; MCP authorization belongs to a separate ordinary review member with only the synthetic MiniGrove Review Demo project. No credentials, browser cookies, OAuth codes or authentication files are in these materials.

This is an edited replay of actual recorded CLI JSONL events, with original tool names, requests, timestamps and results. It is not an uninterrupted screen recording or a recreation of the Codex desktop UI. Browser login/consent is not captured. Pauses and repeated polls are omitted from the video; the selected event projection preserves the tool events and states for each case. The video shows excerpts of longer results.

| Time | Evidence |
|---|---|
| 00:00 | Client, fixture and evidence scope |
| 00:12 | P1: only the authorized project is listed |
| 00:22 | P1: existing supported computer; recovered list-limit refusal disclosed |
| 00:32 | P2: stable-UUID creation request and acceptance receipt |
| 00:44 | P2: preparation and real first execution remain separate |
| 00:56 | P2: exact completed execution and clean Git output |
| 01:10 | P3: artifacts of the exact execution are empty |
| 01:22 | P4: continuation on the same Task and actual follow-up result |
| 01:34 | P5: running command progress before stop |
| 01:46 | P5: stop accepted while acknowledgement remains unobserved |
| 01:56 | P5: target explicitly stopped and worker confirms interruption |
| 02:10 | N1: actual create call refused with insufficient_scope |
| 02:22 | N2: absent project is not guessed or written |
| 02:34 | N3: no merge/publish action; return to MiniGrove workspace |
| 02:46 | Reproducibility and separate official submission gates |

The result projection reports `landing: landed` for a clean, unchanged Task; it does not prove this test merged anything. A stop run's `done` status is terminal; its explicit result establishes interruption, not successful completion of the wait. The creation case's requested final JSON was malformed, so execution acceptance uses structured tool receipts. Earlier guided negative attempts and a stop attempt missing selected-Task context are excluded. An unavailable named project is not a second existing excluded fixture.

The imported five positive and three negative review cases remain in the package manifest. Official browser authorization, tool scanning, publisher verification and final submission must be checked independently.
