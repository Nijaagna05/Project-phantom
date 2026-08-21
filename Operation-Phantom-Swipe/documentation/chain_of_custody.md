\# Chain of Custody



\## Operation Phantom Swipe



All evidence used in this project is fictional and was created for

academic digital-forensics simulation.



| Evidence ID | Item | Date/Time | Collected By | Action |

|---|---|---|---|---|

| PS-01 | ATM Skimmer | 10/08/2026 15:20 | Investigator A | Seized |

| PS-02 | Suspect Mobile Data | 10/08/2026 15:35 | Investigator A | Acquired |

| PS-03 | Skimmer forensic copy | 10/08/2026 16:10 | Forensic Analyst | Imaged |

| PS-04 | Mobile forensic copy | 10/08/2026 16:45 | Forensic Analyst | Imaged |



\## Evidence Handling



The original evidence should be preserved in an unaltered state.

Analysis should be conducted using a forensic working copy whenever

possible.



A write blocker can be used during acquisition of compatible storage

media to prevent accidental modification.



SHA-256 hashes are generated for acquired files to provide an

integrity verification mechanism.



The chain-of-custody record documents the movement and handling of

evidence throughout the simulated investigation.



\## Integrity



The SHA-256 values generated during the investigation are stored in:



`analysis/hashes.txt`

