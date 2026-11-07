#!/usr/bin/env python3
"""STUB — contoh pemakaian konektor Azure DevOps (custom.azure-devops). BELUM TERSAMBUNG.

STATUS — JUJUR, 2026-11-07: PENDING, BELUM ADA KONEKTOR.
Konektor custom.azure-devops BELUM dibuat: link koneksi sudah dikirim ke
Mas Aji dan belum diisi. TIDAK ADA helper di
~/workspace/custom-connectors/custom.azure-devops/bin/ — jangan cari file
itu. File ini adalah stub dokumentasi + kerangka, BUKAN kode yang bisa jalan
sekarang. Jangan menulis token palsu di sini dan jangan pura-pura memanggil
helper yang tidak ada.

RUTE AUTH YANG DIPAKAI: Entra ID OAuth2 authorization code flow
(BUKAN PAT). Microsoft Learn: Azure DevOps hanya menerima PAT lewat HTTP
Basic auth base64(":PAT"), dan bentuk itu tidak bisa dibawa sistem konektor
ini — jadi jalurnya OAuth2:
    issuer:  login.microsoftonline.com (tenant common)
    scope:   499b84ac-1321-427f-aa17-267ca6975798/.default
    redirect: https://agent.meta.ai/api/hatch/oauth/callback
    host:    dev.azure.com, API version 7.1/7.2
Mas Aji harus mendaftarkan aplikasi Entra ID sendiri dan memberi nama
organisasi (org) Azure DevOps-nya.

PANGGILAN PERTAMA SETELAH TERSAMBUNG (verifikasi identitas/koneksi):
    GET https://dev.azure.com/{org}/_apis/connectionData?api-version=7.1
    Auth: Bearer <token Entra ID>
    Sukses menjawab info koneksi + identitas pengguna. Endpoint ini
    read-only dan gratis.

ENDPOINT LAIN (REST API 7.1, semua memakai Bearer token yang sama):
    GET /{org}/_apis/projects?api-version=7.1
        — daftar project di organisasi
    GET /{org}/{project}/_apis/git/repositories?api-version=7.1
        — daftar repo Git di satu project
    GET /{org}/{project}/_apis/build/builds?api-version=7.1
        — riwayat build/pipeline
    GET /{org}/{project}/_apis/wit/workitems/{id}?api-version=7.1
        — baca satu work item

REPO RUJUKAN (sudah di-screening, lihat laporan screening konektor):
    - microsoft/azure-devops-python-api (MIT) — SDK Python resmi, tipis di
      atas REST API; dipakai juga oleh Azure CLI extension. Perlu dicatat:
      perawatannya dipertanyakan komunitas (issue #440) dan rilis terakhir
      membawa client API 7.0/7.1; REST API langsung tetap jalan.
    - microsoft/azure-devops-python-samples (MIT, DIARSIPKAN) — contoh
      pemakaian SDK per area (git, build, work items).
    - Azure/azure-devops-cli-extension (MIT) — ekstensi `az devops` untuk
      Azure CLI; alternatif pemakaian dari baris perintah di VPS.

SETELAH KONEKTOR TERSAMBUNG: ganti file ini dengan wrapper nyata seperti
gitlab_example.py — subprocess ke helper custom.azure-devops + hanya
perintah read-only (connectionData, projects) yang diizinkan default.
Isi {org} dari organisasi Azure DevOps Mas Aji — JANGAN menebak namanya.

File ini TIDAK berisi API key/token/rahasia apa pun.
"""

import sys

# Stub: tidak ada helper, tidak ada panggilan jaringan.
# Menjalankan file ini hanya mencetak status di atas.


def main() -> int:
    print("Konektor custom.azure-devops BELUM tersambung (pending, 2026-11-07).")
    print("Tidak ada helper di ~/workspace/custom-connectors/custom.azure-devops/bin/.")
    print("Rute auth: Entra ID OAuth2 (BUKAN PAT).")
    print("Panggilan pertama setelah tersambung: GET /{org}/_apis/connectionData")
    print("  di dev.azure.com (isi {org} dengan nama organisasi yang benar).")
    print("Lihat docstring file ini untuk detail endpoint dan repo rujukan.")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
