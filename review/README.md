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

These are protocol checks, not native Codex semantic acceptance. The native suite and final recording remain pending the company account's phone-verification step. In particular, the protocol check of a nonexistent out-of-scope ID does not establish a test of a second existing excluded project. The packaged negative prompt checks an absent named project without guessing IDs.

The first unavailable-project assertion expected the wrong error spelling; its failed record was retained before asserting the actual specific code. The first stop happened during setup; it was retained as limited evidence, then repeated with a reported running command and explicit interruption evidence. No failed invocation is presented as a pass.

The sample also contains a tiny Phaser counter with an authenticated members-only preview. It has synthetic data, no formal public release and no merge into the main branch. The read-only protocol Task is called **Protocol read-only workspace check**; native cases create **Read-only workspace check** separately.

## Native walkthrough capture plan

1. Show installing the plugin from a clean Codex client, without an additional chat UI.
2. Show MiniGrove sign-in and consent for only the sample project; keep passwords and OAuth codes outside the frame.
3. Ask for authorized projects and select Review Computer from actual tool output.
4. Create Read-only workspace check once, show preparation, then follow its exact first execution and returned workspace link.
5. Read the result and exact artifacts; an empty artifact list stays empty. Continue the same Task and show the real follow-up result.
6. Start the harmless wait, observe real progress, request a mechanical stop and show the computer acknowledgement.
7. Demonstrate missing creation permission and an unavailable project. Ask for merge/publication and show the human-workspace handoff without issuing either action.

The supplemental video prepared locally uses captured real sample-project screens and clearly identifies the direct protocol harness and company-owner web view. It does not substitute for the pending native Codex recording. Set review.demo_recording_url only after the final reviewer-accessible video is ready. Do not publish the phone-verification page, reviewer password, customer projects, or company-verification documents.

The official company-owned draft remains unsubmitted. Domain proof deployment, official domain verification, MCP authentication/scan, secure reviewer credentials and binding final attestations remain separate gates. Public installation from this repository is not official directory approval.
