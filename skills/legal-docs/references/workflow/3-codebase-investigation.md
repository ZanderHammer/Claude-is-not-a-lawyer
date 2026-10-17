# Phase 3: Codebase investigation

Goal: find out what the software **actually does** with personal data and the user's device, so
the documents describe reality, not the interview's optimism. Every finding needs evidence
(`path:line`). The result is the processing-inventory record (`LDR-0007` in the typical set).

Read the code. Do not run the app, do not call external services, and do not read secret values
(`.env` contents, keys). File and variable *names* are enough to know a service is used.

## 1. Map the project

- Languages, frameworks, monorepo packages, apps (web, mobile, backend, workers).
- Entry points that users touch: pages/routes, API endpoints, mobile screens, e-mails.
- Deployment and hosting: `vercel.json`, `netlify.toml`, `fly.toml`, `Dockerfile`, `serverless.yml`,
  Terraform/Pulumi, GitHub workflows (deploy targets), `app.json`/`eas.json`, `firebase.json`.
- Environment variable **names** in `.env.example`, config schemas, CI secrets references. Names
  like `STRIPE_SECRET_KEY`, `SENTRY_DSN`, `NEXT_PUBLIC_GA_ID` reveal providers.

## 2. Dependencies → third parties

Read manifests and lockfiles (`package.json`, `requirements.txt`/`pyproject.toml`, `Gemfile`,
`composer.json`, `go.mod`, `Cargo.toml`, `pubspec.yaml`, `Podfile`, `build.gradle`). Flag SDKs in
these categories (examples, not exhaustive):

| Category | Typical packages / signals | Why it matters |
|---|---|---|
| Analytics | `@vercel/analytics`, `posthog-js`, `mixpanel`, `@amplitude/*`, `react-ga4`, `gtag`, `plausible`, `matomo`, `@segment/*`, Firebase Analytics | consent (EU-EPRIVACY Art. 5(3)), recipients, transfers |
| Advertising / pixels | Meta Pixel `fbq`, Google Ads, TikTok/LinkedIn insight tags, `gtm` | consent, US "sale/sharing" (US-CA-CCPA) |
| Session replay / heatmaps | `@sentry/replay`, Hotjar, FullStory, Microsoft Clarity, LogRocket | consent, high-risk monitoring |
| Error tracking / logging | `@sentry/*`, Bugsnag, Datadog, LogRocket, Logtail | processor, IP addresses, transfers |
| Auth / identity | Auth0, Clerk, Firebase Auth, Supabase, Cognito, NextAuth providers (Google/GitHub/Apple login) | processors, social login = data from third party (GDPR Art. 14) |
| Payments | Stripe, PayPal, Paddle, Lemon Squeezy, Adyen, Mollie, app-store IAP | payment data, merchant-of-record changes who the contracting party is |
| E-mail / messaging | SendGrid, Postmark, Mailgun, AWS SES, Resend, Mailchimp, Brevo, Twilio | processors, newsletter consent |
| Customer support | Intercom, Zendesk, Crisp, HubSpot, Freshdesk | processors, chat cookies |
| AI / LLM | `openai`, `@anthropic-ai/sdk`, `@google/generative-ai`, Replicate, Hugging Face, vector DBs | user content leaves to a provider, training use, EU-AI-ACT Art. 50 |
| Maps / media embeds | Google Maps, Mapbox, YouTube/Vimeo embeds, social widgets | third-party requests, consent |
| Fonts / CDNs | Google Fonts via `fonts.googleapis.com`, `cdnjs`, `unpkg`, `jsdelivr` | visitor IP addresses go to a third party on every page load; prefer self-hosting |
| Captcha / bot protection | reCAPTCHA, hCaptcha, Cloudflare Turnstile | device data, consent debates |
| Storage / DB / infra | AWS, GCP, Azure, Supabase, Firebase, PlanetScale, Neon, MongoDB Atlas, Cloudflare | processors, hosting region, transfers |
| Push / mobile | Firebase Cloud Messaging, OneSignal, Expo push, AppsFlyer, Adjust | device identifiers, tracking (and ATT on iOS) |
| Feature flags / A/B | LaunchDarkly, Optimizely, GrowthBook, Statsig | identifiers, profiling |

Also search the source (not only manifests) for script tags and URLs loaded at runtime:
`<script src=`, `googletagmanager`, `connect.facebook.net`, `fonts.googleapis`, `youtube.com/embed`,
`maps.googleapis`, iframes, and image/pixel URLs to third-party domains.

## 3. Device storage and tracking (cookie policy input)

Search for: `document.cookie`, `cookies()` / `setCookie` / `res.cookie`, `localStorage`,
`sessionStorage`, `indexedDB`, service workers, `navigator.` fingerprinting signals, SDK
initialisation that sets cookies (`gtag('config'`, `posthog.init`). For each item record name
(if known), purpose, first/third party, duration, and whether it is **strictly necessary** for a
service the user explicitly requested (exemption in EU-EPRIVACY Art. 5(3), DE-TDDDG § 25(2) Nr. 2,
AT-TKG-165, UK-PECR Sch. A1). Check whether a consent banner exists and whether non-essential
scripts actually **wait** for consent (look at the loading logic, not the banner text).

## 4. Personal data the app collects itself

- Database schemas and models (Prisma, TypeORM, Django models, SQL migrations, Firestore rules):
  list fields that are personal data (name, e-mail, address, phone, IP, device IDs, location,
  payment references, birthdates, free-text fields, uploaded files, special categories).
- Forms and inputs (sign-up, checkout, contact, newsletter, profile, support). Note which fields
  are mandatory.
- Server logs and request logging (IP addresses, user agents), analytics events with user IDs.
- Authentication and session handling, account deletion flows (does deletion exist?).
- Data exports, admin panels, background jobs that send data elsewhere.
- Retention: TTLs, cron cleanups, soft-delete flags. Missing deletion → note it as a gap.

## 5. Contract and consumer-law signals (terms input)

Pricing pages, checkout flows, subscription logic (trials, renewals, cancellation endpoint),
order button labels (EU-CRD Art. 8(2), DE-BGB-FERNABSATZ § 312j), cancellation button
(DE-BGB-FERNABSATZ § 312k), withdrawal function (EU-CRD Art. 11a, DE-BGB-WIDERRUF § 356a,
AT-FAGG § 13a), user-generated content features (upload, comments, profiles), moderation tools,
reporting/flagging features (EU-DSA Art. 16), age gates.

## 6. Existing legal texts in the repo

Search for existing privacy policies, terms, imprint pages, cookie banners, consent configs and
footer links. They show what the user already promised publicly. Differences to the new drafts
must be explained in the defense report.

## 7. Write the inventory record

For each processing activity: purpose, data categories, data subjects, source (user / third
party / automatically), legal basis candidate (to be argued in phase 5), recipients/processors
with their role, third-country transfer (country, mechanism candidate), retention, evidence
(`path:line`), and whether it needs consent. Then list:

- **Contradictions with the interview** → ask the user (interview rules apply).
- **Compliance gaps in the code** (e.g. analytics loads before consent, no account deletion, no
  withdrawal button, remote Google Fonts). The documents must not paper over these. Tell the user
  plainly that a document cannot fix a code problem, record each gap, and offer to fix the code
  in a separate task.
- **Unknowns** that the code cannot answer (hosting region of a managed service, whether a DPA
  exists with a provider) → ask.

Set the record to `accepted` only after the user confirmed the inventory.
