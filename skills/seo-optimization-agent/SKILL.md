---
name: seo-optimization-agent
description: Guides agents through SEO content optimization, keyword strategy, and SERP analysis. Use when optimizing blog posts for organic search, generating keyword strategies, or auditing content for SEO performance.
---

# SEO Optimization Agent

## Overview
Analyzes blog post content and generates comprehensive SEO optimization reports. In a second pass, produces an optimized HTML blog post. Integrates with Notion via webhook for content ingestion and result delivery.

## When to Use
- Optimizing blog posts for organic search performance
- Generating keyword strategies for content marketing
- Auditing existing content for SEO gaps
- Creating optimized HTML from raw content
- NOT for: technical SEO (use `security-and-hardening`), performance optimization (use `performance-optimization`)

## Process

### Pass 1: SEO Audit & Report

#### 1. Analyze Input Content
- Receive blog post data (webhook from Notion or text file)
- Extract: title, body, meta description, existing keywords, URL slug
- Identify content length, heading structure, internal/external links

#### 2. Keyword Research & Strategy
- Identify primary keyword and 3-5 secondary keywords
- Analyze search intent (informational, navigational, transactional)
- Check keyword density and placement
- Suggest long-tail keyword opportunities

#### 3. On-Page SEO Audit
| Element | Check |
|---|---|
| Title tag | Length (50-60 chars), keyword placement, clickability |
| Meta description | Length (150-160 chars), call-to-action, keyword inclusion |
| Headings | H1-H6 hierarchy, keyword distribution |
| Content | Readability score, keyword density (1-2%), word count |
| Images | Alt text, file names, compression |
| URLs | Slug optimization, structure |

#### 4. Content Optimization Report
Generate structured report with:
- Current score (0-100)
- Keyword recommendations with search volume estimates
- Heading and structural improvements
- Missing elements (schema markup, canonical, etc.)
- Priority actions (Critical, High, Medium, Low)

### Pass 2: Optimized HTML Generation

#### 1. Apply SEO Recommendations
- Rewrite title tag and meta description
- Restructure headings (H1-H6)
- Optimize keyword placement
- Add internal/external link opportunities
- Insert schema markup (Article, BlogPosting)

#### 2. Generate Final HTML
- Semantic HTML5 structure
- SEO-optimized meta tags
- Open Graph and Twitter Card tags
- JSON-LD structured data
- Mobile-friendly responsive markup

#### 3. Deliver Results
- Upload optimization report (URL)
- Upload final HTML post (URL)
- Update original Notion record with both URLs

## Usage

This skill ships automation scripts:

```bash
# Run SEO audit on content file
bash scripts/seo-audit.sh input.txt --output report.json

# Generate optimized HTML
bash scripts/generate-html.sh report.json --output post.html
```

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "SEO is just keywords now" | Technical SEO, structured data, and user intent matter more than ever |
| "AI content doesn't need SEO" | AI-generated content must be optimized for discovery just like any content |
| "I'll add meta tags later" | Meta tags are critical for CTR; add them during creation |
| "Keyword stuffing works" | Google penalizes over-optimization; natural language wins |

## Red Flags
- No keyword research before writing
- Missing meta description or title tag
- No heading hierarchy (H1 > H2 > H3)
- Zero internal links
- No schema markup for content type
- Images without alt text

## Verification
- [ ] Primary keyword in title tag (near beginning)
- [ ] Meta description with keyword + CTA
- [ ] H1 contains primary keyword
- [ ] H2/H3 structure is logical and keyword-aware
- [ ] Content has internal links (2-3)
- [ ] Images have descriptive alt text
- [ ] Open Graph tags present
- [ ] JSON-LD structured data included
- [ ] Mobile-responsive HTML output
