# Writing Guidelines

Content voice, style rules, and forbidden patterns.

---

## 1. Voice Principles

### Be Direct

Say what you mean. Cut the preamble.

| Avoid | Prefer |
|-------|--------|
| "We are pleased to announce that..." | "Announcing..." |
| "It is important to note that..." | (just state the fact) |
| "In order to..." | "To..." |
| "At this point in time..." | "Now..." |

### Be Specific

Numbers beat adjectives. Evidence beats claims.

| Avoid | Prefer |
|-------|--------|
| "Significant growth" | "42% growth" |
| "Industry-leading" | "Fastest in benchmark X" |
| "Many customers" | "12,000 customers" |
| "Recently launched" | "Launched October 2024" |

### Be Active

Subject does action. Passive obscures responsibility.

| Avoid | Prefer |
|-------|--------|
| "The feature was shipped" | "We shipped the feature" |
| "Errors are handled by..." | "The router handles errors" |
| "It was decided that..." | "We decided..." |

---

## 2. Headline Rules

### Slide Titles Assert, Don't Label

Headlines should make a claim, not name a category.

| Label (avoid) | Assertion (prefer) |
|---------------|-------------------|
| "Q3 Results" | "Revenue up 23% in Q3" |
| "Product Overview" | "One workspace for all your work" |
| "Customer Feedback" | "Customers rate us 4.9/5" |
| "Next Steps" | "Launch enterprise tier by Q1" |

### Section Heads

Use sentence case. No periods. 2-6 words.

| Avoid | Prefer |
|-------|--------|
| "WHAT WE DO" | "What we do" |
| "Our Amazing Features." | "Features" |
| "Here's Why Customers Love Us" | "Why teams choose us" |

---

## 3. Numbers and Data

### Formatting

| Type | Format | Example |
|------|--------|---------|
| Large numbers | Abbreviate with K/M/B | 12K users, $4.2M |
| Percentages | No decimal unless needed | 23%, not 23.00% |
| Money | Currency symbol, abbreviate | $4.2M, not $4,200,000 |
| Dates | ISO or written | 2024-10-15 or October 15, 2024 |
| Times | 24h or with AM/PM | 14:00 or 2:00 PM |
| Ranges | En dash, no spaces | 10-15, not 10 - 15 |

### Tabular Data

Right-align numbers. Use `tabular-nums` for alignment.

```css
.num {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

### Metrics

Always pair numbers with context:
- "40% faster" → faster than what?
- "$4.2M revenue" → what period?
- "12K users" → daily? monthly? total?

---

## 4. Lists

### Parallel Structure

All items should be the same grammatical form.

**Wrong**:
- Improves performance
- Easy to use
- You can customize it

**Right**:
- Improves performance
- Simplifies workflows
- Enables customization

### Length

- 3-7 items is ideal
- If >7, consider grouping or a table
- Each item: 1-2 lines max

### Punctuation

- No periods for single phrases
- Periods for complete sentences
- Consistent within each list

---

## 5. Forbidden Words and Phrases

### Corporate Jargon (never use)

| Word | Why | Alternative |
|------|-----|-------------|
| Leverage | Overused, vague | Use, apply |
| Synergy | Meaningless | Collaboration, integration |
| Unlock | Marketing speak | Enable, allow |
| Empower | Patronizing | Help, enable |
| Disrupt | Overpromises | Change, improve |
| Scalable | Vague without context | "Handles 100K requests" |
| Robust | Meaningless | Reliable, tested |
| Seamless | Usually false | Integrated, automatic |
| Best-in-class | Unverifiable | (cite specific benchmark) |
| World-class | Meaningless | (cite specific achievement) |

### Filler Phrases (delete entirely)

- "It goes without saying..."
- "Needless to say..."
- "As you know..."
- "To be honest..."
- "At the end of the day..."
- "Moving forward..."
- "In terms of..."
- "With that being said..."

### Weak Openers (rewrite)

- "There is/are..."
- "It is..."
- "This is..."
- "What we do is..."

---

## 6. Punctuation

### Em Dashes

Avoid em dashes (—). Use commas, colons, or separate sentences.

| Avoid | Prefer |
|-------|--------|
| "The feature—which launched last month—works" | "The feature, which launched last month, works" |
| "One goal—shipping faster" | "One goal: shipping faster" |

### Exclamation Points

Never in body copy. Rarely in headlines. The content should convey excitement.

### Ellipses

Never use for trailing off. Only for omitted text in quotes.

### Colons

Use to introduce lists or explanations. Capitalize after only if complete sentence.

---

## 7. Technical Writing

### Code References

Use backticks for inline code: `function_name`, `--token-name`.

### API Documentation

- Document what, not how to implement
- Include request/response examples
- Version all breaking changes

### Error Messages

| Bad | Good |
|-----|------|
| "Error occurred" | "Could not save: file already exists" |
| "Invalid input" | "Email address must include @" |
| "Operation failed" | "Payment declined: insufficient funds" |

---

## 8. Localization Readiness

### String Preparation

- Avoid concatenating strings
- Use complete sentences
- Don't embed numbers in strings
- Avoid idioms and puns

| Avoid | Prefer |
|-------|--------|
| "You have " + n + " items" | "Items: {count}" |
| "Kill two birds with one stone" | "Solve both problems at once" |
| "It's a piece of cake" | "It's simple" |

### Cultural Sensitivity

- Dates: Use ISO 8601 or spell out month
- Currency: Show symbol and code
- Names: Don't assume first/last order
- Colors: Meanings vary by culture

---

## 9. Resume/Portfolio Specific

### Action Verbs

Start bullets with strong verbs:

**Building**: Built, Created, Designed, Developed, Implemented, Launched

**Impact**: Reduced, Increased, Improved, Accelerated, Streamlined

**Leadership**: Led, Managed, Coordinated, Mentored, Directed

### Avoid

- "Responsible for..." (passive)
- "Helped with..." (vague)
- "Various tasks..." (lazy)
- "Etc." (incomplete)

### Quantify Impact

| Weak | Strong |
|------|--------|
| "Improved performance" | "Reduced load time from 4s to 0.8s" |
| "Led a team" | "Led 8-person engineering team" |
| "Worked on payments" | "Processed $2M daily transactions" |

---

## 10. Review Checklist

Before shipping content:

- [ ] No forbidden words or phrases
- [ ] All claims have evidence
- [ ] Numbers have context
- [ ] Headlines assert, not label
- [ ] Lists are parallel
- [ ] Active voice throughout
- [ ] No em dashes or exclamation points
- [ ] Technical terms defined or linked
- [ ] Spell-checked
- [ ] Read aloud (catches awkward phrasing)
