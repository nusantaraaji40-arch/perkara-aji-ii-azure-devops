# Contoh Konektor Azure DevOps — PERKARA AJI II

Contoh pemakaian konektor Azure DevOps (custom.azure-devops) dari workspace Muse. **Repo ini masih berupa stub** — konektornya belum tersambung, jadi file contoh di sini adalah dokumentasi + kerangka, bukan kode yang sudah bisa jalan. Repo ini bagian dari proyek PERKARA AJI II — agen AI yang membuat video YouTube 8 menit dari foto presenter.

## Isi repo

| File | Konektor | Keterangan |
|---|---|---|
| `azure_devops_example.py` | custom.azure-devops (belum ada) | Stub jujur — hanya mencetak status; tidak ada panggilan jaringan |

## Rute auth yang dipakai: Entra ID OAuth2 (BUKAN PAT)

Microsoft Learn: Azure DevOps hanya menerima PAT lewat HTTP Basic auth base64(`:PAT`), dan bentuk itu tidak bisa dibawa sistem konektor ini — jadi jalurnya OAuth2 authorization code flow via Microsoft Entra ID:

- Issuer: `login.microsoftonline.com` (tenant `common`)
- Scope: `499b84ac-1321-427f-aa17-267ca6975798/.default`
- Redirect URI: `https://agent.meta.ai/api/hatch/oauth/callback`
- Host: `dev.azure.com`, API version 7.1/7.2

Yang harus disiapkan dulu: app registration di Microsoft Entra ID (portal.azure.com → Entra ID → App registrations) dengan Redirect URI di atas, plus API permission Azure DevOps `user_impersonation`. Nama organisasi Azure DevOps juga dibutuhkan untuk panggilan API.

## Status — jujur (2026-11-07)

**PENDING, belum tersambung.** Folder konektor belum ada, tidak ada helper. Link koneksi sudah dikirim dan belum diisi. Setelah tersambung, file contoh ini harus diganti dengan wrapper nyata seperti `gitlab_example.py` (subprocess ke helper + hanya perintah read-only yang diizinkan default).

## Panggilan pertama setelah tersambung (verifikasi identitas/koneksi)

```bash
GET https://dev.azure.com/{org}/_apis/connectionData?api-version=7.1
```

Auth: `Authorization: Bearer <token Entra ID>`. Isi `{org}` dengan nama organisasi Azure DevOps yang benar — jangan menebak. Endpoint lain (REST API 7.1): `GET /{org}/_apis/projects`, `GET /{org}/{project}/_apis/git/repositories`, `GET /{org}/{project}/_apis/build/builds`, `GET /{org}/{project}/_apis/wit/workitems/{id}`.

## Tanpa secret

File-file di repo ini **tidak berisi API key, token, atau rahasia apa pun**. Jangan pernah menaruh token di file, di `.env`, atau di commit.

## Repo terkait (hasil screening)

Repo open source terbaik untuk memakai Azure DevOps API dari code sendiri (bukan bagian repo ini, lisensinya masing-masing):

- **azure-devops-python-api** — https://github.com/microsoft/azure-devops-python-api — SDK Python resmi (thin wrapper REST API): git, build/pipeline, work items, release, lisensi MIT. Catatan: perawatannya dipertanyakan komunitas (issue #440), tapi rilis terakhir membawa client API 7.0/7.1.
- **azure-devops-python-samples** — https://github.com/microsoft/azure-devops-python-samples — contoh pemakaian SDK per area, lisensi MIT. Catatan: repo ini **diarsipkan** Microsoft, jadi contohnya bisa usang.
- **azure-devops-cli-extension** — https://github.com/Azure/azure-devops-cli-extension — ekstensi `az devops` untuk Azure CLI, lisensi MIT. Alternatif pemakaian dari baris perintah di VPS.

Catatan: SDK Node resmi (`microsoft/azure-devops-node-api`) tidak dipakai — file LICENSE-nya berbunyi "All rights reserved" (proprietary).

## Lisensi

Code contoh di repo ini berlisensi **MIT** (lihat `LICENSE`). Dependensi/repo terkait di atas punya lisensinya sendiri-sendiri — periksa sebelum memakai.
