# Directory review preparation

Version 0.2.2 imports five positive and three negative cases from the package manifest. The JSON copy beside this file is for reviewer planning; the manifest is what the portal imports. No credentials or private reviewer instructions are included here or in the distributable ZIP.

## Evidence from 2026-10-27

The dedicated email-verified reviewer was an ordinary member of one synthetic production project, **MiniGrove Review Demo**, with **Review Computer**. Password login was tested. Separate full and read-only MCP grants selected only that project. All nine advertised tools were discovered.

| Case | Direct MCP protocol result |
|---|---|
| Discover projects, computer and Tasks | Passed; exactly the selected sample project |
| Create Task, retry identical request, follow first execution | Passed; same UUID returned the same Task; actual clean Git output |
| Read conversation and artifacts of exact execution | Passed; no artifact invented for the read-only run |
| Continue same Task | Passed; follow-up marker and clean Git output |
| Stop running command | Passed; command progress observed, worker confirmed forced interruption, target explicitly stopped |
| Create with read-only grant | Refused with insufficient_scope |
| Read unselected nonexistent fixture ID | Refused with project_unavailable |
| Merge/publish native slash controls | Both refused; neither tool is advertised |

The same five positive and three negative workflows subsequently passed in real native Codex CLI 0.156.1, using a fresh company-account sign-in and the review member's sample-only MCP grants. The model was gpt-6-luna, selected from that account's actual model catalog. The CLI created one separate **Read-only workspace check** Task, followed its exact first execution, read its empty artifacts, continued it, and stopped it after observing a reported command step. With a separate read-only grant, the real creation call returned insufficient_scope and the final answer linked connection management. The unavailable-project and merge/publication prompts produced no write calls.

Native execution evidence was checked against the structured tool receipts, not just the CLI's zero exit status. An [edited native CLI evidence walkthrough](assets/minigrove-native-codex-walkthrough.mp4) now shows the actual prompts and tool receipts for all eight cases; the [selected receipts and source hashes](assets/native-walkthrough-evidence.json) accompany it. This is an edited replay, not an uninterrupted screen recording, desktop UI capture or OAuth browser-consent recording. The protocol check of a nonexistent out-of-scope ID does not establish a test of a second existing excluded project; the native negative prompt checks an absent named project without guessing IDs.

Retained native limitations: the initial selected model was unavailable to the company account; a list limit of 100 was refused and the client recovered with 50. Initial negative prompts included expected behavior and were excluded, then rerun as plain user requests. Independent conversations initially lacked the selected-Task context for stopping, so the stop case was repeated with that fixture identity explicit. The creation case's requested final JSON was malformed; its actual structured MCP receipts still establish creation and execution. No failed or guided invocation is counted as independent acceptance.

The first unavailable-project assertion expected the wrong error spelling; its failed record was retained before asserting the actual specific code. The first stop happened during setup; it was retained as limited evidence, then repeated with a reported running command and explicit interruption evidence. No failed invocation is presented as a pass.

The sample also contains a tiny Phaser counter with an authenticated members-only preview. It has synthetic data, no formal public release and no merge into the main branch. The read-only protocol Task is called **Protocol read-only workspace check**; native cases create **Read-only workspace check** separately.

## Additional browser-consent capture plan

1. Show installing the plugin from a clean Codex client, without an additional chat UI.
2. Show MiniGrove sign-in and consent for only the sample project; keep passwords and OAuth codes outside the frame.
3. Ask for authorized projects and select Review Computer from actual tool output.
4. Create Read-only workspace check once, show preparation, then follow its exact first execution and returned workspace link.
5. Read the result and exact artifacts; an empty artifact list stays empty. Continue the same Task and show the real follow-up result.
6. Start the harmless wait, observe real progress, request a mechanical stop and show the computer acknowledgement.
7. Demonstrate missing creation permission and an unavailable project. Ask for merge/publication and show the human-workspace handoff without issuing either action.

The supplemental video prepared locally uses captured real sample-project screens and clearly identifies the direct protocol harness and company-owner web view. It is separate from the native CLI evidence replay. The walkthrough URL remains editable in the portal; credentials are supplied only through private reviewer fields. Do not publish the phone-verification page, reviewer password, customer projects, or company-verification documents.

The official company-owned 0.2.2 submission is now in review, as recorded below. The domain proof deployed successfully through server PR #1174 and its public response was verified byte-for-byte. On 2026-10-28 UTC the official portal reported **Domain verified** for the company-owned 0.2.2 draft, with metadata **No findings**, the skill **Checks passed**, and all five positive plus three negative cases imported complete. The dedicated credentials and sign-in instructions were saved only in OpenAI's private reviewer fields, and the pinned public video URL was saved in supporting content; all five review-information steps show complete. Organization settings now show **Verified**, with **Business: Approved**.

Official OAuth setup exposed a 757-character relay state rejected by the server's 512-character limit. [Server PR #1178](https://github.com/muyigames/minigrove-server/pull/1178) is now merged and both production services deployed successfully. The official draft completed authorization as the dedicated ordinary review member, selecting only MiniGrove Review Demo, and discovered all nine tools.

The completed official scan reported one finding: `minigrove_stop_conversation` advertised `destructiveHint: false` despite potentially force-interrupting work. [Server PR #1179](https://github.com/muyigames/minigrove-server/pull/1179) corrects all three write tools' eventual-effect annotations and explains file changes and interruption in English and Chinese; the six read tools remain non-destructive. Full typecheck/build, 238 focused regression tests and four mutation expectations passed, with one optional external MiniHug fixture skipped. This fix is now merged at `92e994acaed6e9fb7eeb25bcdae3f716d7ff7013`, both production services deployed successfully, and the new official scan completed at 2026-10-27 6:33:49 PM America/Los_Angeles. The portal reports **No findings in the latest MCP scan**, with all nine tools discovered; the scanned stop definition contains the updated description and `destructiveHint: true`. Metadata and skill checks also pass. After the owner explicitly confirmed all six final declarations, MiniGrove 0.2.2 was submitted under Muyi Games, Inc. The official portal now reports **In review**, with **Publication: Not published**. Official release reference: `pluginrel_761738d90e88819198dc3b5bba99eae9`. Public installation from this repository is not official directory approval.
