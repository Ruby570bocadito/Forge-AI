# AIHACK — AI-Powered Pentesting Suite

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-00FF88?logo=ollama&logoColor=white)](https://ollama.ai)
[![License](https://img.shields.io/badge/License-MIT-FF6600)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux_|_macOS_|_Windows-0078D6)]()

**AIHACK** is a CLI-based autonomous pentesting suite powered by local AI models (Ollama, LM Studio, Llama.cpp). It combines AI-driven reasoning with real security tools — nmap, vulnerability scanners, OSINT APIs, CVE databases, and more — into a single terminal interface.

---

## Architecture

```
User → AIHACK CLI → Local LLM (Ollama/LM Studio/Llama.cpp)
                         ↓
              Autonomous Agent + 17 Security Modes
                         ↓
   ┌──────────┬──────────┬──────────┬──────────┬──────────┐
   │  Recon   │  Vuln    │  OSINT   │ Exploit  │ Forense  │
   │  Scans   │  CVE DB  │  APIs    │  Search  │  Blue    │
   └──────────┴──────────┴──────────┴──────────┴──────────┘
```

## Features

| Feature | Description |
|---------|-------------|
| **17 Operation Modes** | Autonomous, Pentester, Blue Team, OSINT, Forense, Bug Bounty, Red Team, Vuln Assessment, Network, Web App, Social Engineering, DevSecOps, Malware Analysis, IoT, Cloud, Mobile, Compliance |
| **Autonomous Agent** | AI-driven workflows with chain-of-thought reasoning, auto-execution, and memory |
| **Multi-Backend** | Ollama, LM Studio, Llama.cpp — switch on the fly |
| **Scan Engine** | Quick, full, stealth, vulnerability, web, directory, OS detection scans via nmap/Nikto/WhatWeb |
| **CVE Database** | Offline CISA KEV integration, keyword search, recent exploits |
| **OSINT APIs** | Shodan, VirusTotal, Hunter.io, CRT.SH, Whois |
| **Threat Intelligence** | IOC extraction, threat classification, IP reputation, hash analysis |
| **Compliance** | CIS Benchmarks, OWASP Top 10, PCI-DSS, NIST Framework checks |
| **Incident Response** | Incident lifecycle, response steps, escalation workflows |
| **Code Generation** | AI-generated shells, payloads, scripts, and tools |
| **Session Management** | Persistent sessions, target tracking, result history |
| **Report Generation** | Quick reports, HTML/PDF exports, markdown summaries |
| **Rich Terminal UI** | Color-coded panels, tables, status bars with Rich library |
| **Runs Offline** | 100% local after initial model pull — no cloud dependency |

## Quick Start

```bash
# 1. Clone
git clone https://github.com/Ruby570bocadito/AIHACK.git
cd AIHACK

# 2. Install
pip install -r requirements.txt

# 3. Ensure Ollama is running
ollama serve

# 4. Pull a model
ollama pull llama3.2

# 5. Launch interactive mode
python main.py

# Or install as CLI tool
pip install -e .
aihack
```

## CLI Commands

### Scanning
| Command | Description |
|---------|-------------|
| `/scan <target>` | Quick nmap scan |
| `/full <target>` | Full port scan |
| `/vuln <target>` | Vulnerability scan |
| `/web <target>` | Web app scan (Nikto + WhatWeb) |
| `/dir <target>` | Directory enumeration |
| `/stealth <target>` | IDS/Firewall evasion scan |
| `/os <target>` | OS detection |

### Enumeration
| Command | Description |
|---------|-------------|
| `/enum <target>` | Full enumeration |
| `/dns <domain>` | DNS record enumeration |
| `/subdomain <domain>` | Subdomain discovery |
| `/autopwn <target>` | Automated pentest |
| `/fullpentest <target>` | 8-phase full pentest |

### OSINT & APIs
| Command | Description |
|---------|-------------|
| `/shodan <IP>` | Shodan lookup |
| `/virus <domain>` | VirusTotal scan |
| `/hunter <domain>` | Email discovery |
| `/crt <domain>` | SSL certificate search |
| `/whois <domain>` | Whois lookup |

### Threat Intel & CVE
| Command | Description |
|---------|-------------|
| `/cve <id\|keyword>` | CVE search by ID or keyword |
| `/cveupdate` | Update CISA KEV database |
| `/recent` | Recent exploits (30 days) |
| `/ioc <text>` | Extract IOCs from text |
| `/threat <type>` | Classify threats |
| `/reputation <IP>` | IP reputation check |

### Compliance & Incident Response
| Command | Description |
|---------|-------------|
| `/compliance <cis\|owasp\|pci\|nist>` | Compliance audit |
| `/headers <domain>` | Security headers check |
| `/incident <type>` | Create incident |
| `/ir-steps <type>` | Response playbook |
| `/escalate <severity>` | Escalate incident |

### Code Generation
| Command | Description |
|---------|-------------|
| `/code <desc>` | Generate code/script |
| `/shell <type>` | Generate reverse/bind shell |
| `/payload <type>` | Generate payload |
| `/script <desc>` | Create automation script |

### System & Sessions
| Command | Description |
|---------|-------------|
| `/mode <name>` | Switch mode |
| `/modes` | List all 17 modes |
| `/models` | List available LLMs |
| `/backend <name>` | Switch backend |
| `/session <name>` | Create/list sessions |
| `/resume <name>` | Resume session |
| `/history` | View chat history |
| `/run <cmd>` | Execute system command |
| `/report <target>` | Generate report |
| `/reporthtml <target>` | HTML report |

### Agent
| Command | Description |
|---------|-------------|
| `/agent <task>` | Run autonomous agent |
| `/workflow <name> <target>` | Run predefined workflow |
| `/status` | Agent status |
| `/summary` | Activity summary |
| `/skills` | List available skills |

## Operation Modes

```
[A]  Autonomous       — Self-directed agent with chain-of-thought reasoning
[P]  Pentester        — Offensive security, exploitation, PTES methodology
[B]  Blue Team        — Defense, threat hunting, incident response
[O]  OSINT            — Passive intelligence gathering, reconnaissance
[F]  Forense          — Digital forensics, evidence analysis
[BB] Bug Bounty       — Vulnerability hunting, OWASP Top 10
[RT] Red Team         — Adversary simulation, MITRE ATT&CK
[VA] Vuln Assessment  — Vulnerability scoring (CVSS), prioritization
[N]  Network          — Infrastructure security, segmentation
[W]  Web App          — Web pentesting, API testing
[SE] Social Engineering — Phishing, vishing, awareness
[DS] DevSecOps        — CI/CD security, SAST, DAST, containers
[M]  Malware Analysis — Static/dynamic analysis, reverse engineering
[IoT] IoT Security    — Protocol analysis, firmware, BLE/Zigbee
[C]  Cloud Security   — AWS, Azure, GCP misconfig audit
[Mob] Mobile Security — Android/iOS APK/IPA analysis
[Comp] Compliance     — HIPAA, PCI-DSS, ISO 27001 audits
```

## Workflows

AIHACK includes predefined autonomous workflows:

| Workflow | Steps |
|----------|-------|
| `recon` | Whois → Subdomain enum → Port scan → Shodan |
| `vuln_assess` | Port scan → Vuln scan → Web scan |
| `web_assess` | Tech detection → Dir enum → Vuln scan |
| `full_pentest` | 5-phase PTES methodology |
| `quick_recon` | Whois → Quick scan → Shodan |

## Requirements

- **Python** 3.10+
- **Ollama** (or LM Studio, Llama.cpp) running locally
- At least one Ollama model pulled (`ollama pull llama3.2`)
- **Optional**: nmap, Nikto, WhatWeb for scan capabilities
- **Optional API keys**: Shodan, VirusTotal, Hunter.io (set via environment variables)

## Project Structure

```
AIHACK/
├── main.py                   # Entry point with argparse CLI
├── src/
│   ├── cli_app.py            # Main interactive CLI (Typer + Rich)
│   ├── cli_theme.py          # Color palette and theme system
│   ├── ollama_client.py      # Ollama/LM Studio/Llama.cpp client
│   ├── ai/
│   │   ├── agent.py          # Autonomous agent + workflows
│   │   ├── prompts.py        # System prompts per mode
│   │   ├── skills.py         # Skill definitions
│   │   ├── workflows.py      # Workflow definitions
│   │   └── backends/         # Multi-backend support
│   ├── modes/
│   │   ├── mode_manager.py   # Mode persistence (17 modes)
│   │   └── prompts.py        # Specialized prompts per mode
│   ├── tools/
│   │   ├── pentest.py        # Scan engine (nmap, nikto, sqlmap)
│   │   ├── system.py         # System commands and utilities
│   │   ├── apis.py           # Shodan, VirusTotal, Hunter, CRT.SH
│   │   ├── cve.py            # CISA KEV database integration
│   │   ├── compliance.py     # CIS, OWASP, PCI, NIST checks
│   │   ├── threat_intel.py   # IOC extraction, threat classification
│   │   ├── incident_response.py # Incident management
│   │   ├── security.py       # Input sanitization, validation
│   │   ├── metrics.py        # Security metrics tracking
│   │   ├── sessions.py       # Session persistence
│   │   ├── history.py        # Chat history
│   │   ├── vuln_db.py        # Local vulnerability database
│   │   ├── analyzer.py       # Scan output analysis
│   │   └── ...
│   ├── config/
│   │   ├── config.py         # Pydantic configuration manager
│   │   └── settings.py       # Settings and API keys
│   ├── reports/
│   │   └── generator.py      # HTML/MD report generation
│   ├── cli_commands/         # Command dispatchers
│   ├── logging_config.py     # Structured logging
│   ├── validators.py         # Pydantic input validation
│   ├── project_types.py      # Shared type definitions
│   ├── plugins.py            # Plugin system
│   └── i18n.py               # Internationalization (es, pt)
├── tests/                    # Test suite (pytest)
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama API endpoint |
| `DEFAULT_BACKEND` | `ollama` | Backend selection |
| `DEFAULT_MODEL` | `llama3.2` | Default LLM model |
| `SHODAN_API_KEY` | — | Shodan API key |
| `VIRUSTOTAL_API_KEY` | — | VirusTotal API key |
| `HUNTER_API_KEY` | — | Hunter.io API key |
| `OUTPUT_DIR` | `output` | Output directory |
| `AIHACK_DEBUG` | `false` | Enable debug mode |

## Docker

```bash
docker build -t aihack .
docker run -it --rm \
  -e OLLAMA_HOST=http://host.docker.internal:11434 \
  aihack
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Type checking
mypy src/

# Code formatting
black src/ tests/
isort src/ tests/
```

## License

MIT — Free to use, modify, and distribute.
