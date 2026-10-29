---
name: first-principles
description: First-principles reasoning for any problem where the accepted answer, cost, limit or plan may rest on convention rather than fact. Use when the user says "first principles", asks why something is done a certain way, challenges an estimate or "it can't be done", or when a dev, product or strategy decision is stuck on analogy to what others do.
---

# First principles

Break a problem down until each remaining piece is either a verified fact or a named assumption, then rebuild a solution from the facts alone. The opposite move is **reasoning by analogy**: "we do it this way because it is how it has been done" or "nobody does that, so it must be bad". Analogy is cheap and usually fine. First principles costs more effort, so spend it where the accepted answer is expensive, stuck, or built for an environment that has changed.

A **first principle** here is whatever is irreducible *in this context*, not an absolute truth. For a fridge's efficiency, the laws of thermodynamics are first principles; a physicist studying entropy would go further down. Go one or two levels deeper than the existing solution. That is usually where the value is, and going to the atomic level rarely pays.

Source: Farnam Street, [First Principles](https://fs.blog/first-principles/). Read [`APPLICATIONS.md`](APPLICATIONS.md) for the dev, product and strategy playbooks and the worked examples from the article.

## Steps

Write the output of each step into the working note (format at the end). Each step ends on its criterion.

1. **State the goal as an outcome.** Name what must be true when the problem is solved, without naming the current solution. "Get people to Mars" leads to "rockets must cost far less"; "build a faster ETL" is a solution wearing a goal's clothes. *Done when the goal sentence would still hold if every existing tool and process disappeared.*

2. **List the accepted answer and every claim under it.** Write down the current approach and each reason people give for it: costs, limits, "users want", "we must", "it is impossible", "industry standard". *Done when every claim that supports the accepted answer is on the list, including the ones that feel obvious.*

3. **Decompose into the Lego blocks.** Break the system into its parts (a bike is a seat, chain, frame, handlebars), then break the parts down one level further where it matters (cost into materials, latency into I/O and compute, a market into buyers and their budgets). *Done when each part is either irreducible in this context or broken down two levels below the existing solution.*

4. **Sort fact from shared belief.** For every claim and part, run Socratic questioning and the Five Whys (below) until it lands in one of two bins:
   - **Fact**: a law of nature, a measurement, or data you can cite. Record the source.
   - **Assumption**: a convention, a shared belief, an authority's say-so, or a "why" chain that ended in "I don't know". Everything that is not a law of nature or a measurement is a shared belief, however widely held.
   
   *Done when every claim carries a bin and every fact carries a source.*

5. **Price the floor.** Using only the facts, compute the best the physics, data or economics allows: the cost of the raw materials, the minimum bytes moved, the number of users who actually hit the problem. Musk priced a battery's cobalt, nickel, aluminium, carbon and steel at spot prices and got about $80/kWh against an accepted $600/kWh. The gap between the floor and the accepted answer is the opportunity, and the assumptions from step 4 explain it. *Done when the floor is a number with its working, or the note says why no number is possible.*

6. **Rebuild from the facts.** Generate solutions that satisfy the goal and the facts while dropping the assumptions. Include at least one that is not an iteration of the existing approach: rearranging the Lego house is first-layer thinking, building something else from the bricks is the point. *Done when there is at least one option that departs structurally from the accepted answer, and each option names which assumption it drops.*

7. **Try to falsify each option.** Ask what happens if the conclusion is wrong: which assumption, if true after all, kills the option, and what is the cheapest test of it. Knowledge holds only while you are actively trying to break it. *Done when every option has its killing assumption and a concrete test to run first.*

## Questioning tools

**Socratic questioning** works through a claim in this order:

1. Clarify: what exactly do I think, and why do I think it?
2. Challenge the assumption: how do I know this is true? What if the opposite were true?
3. Evidence: what backs it up, and what is the source?
4. Alternative views: what would someone who disagrees say?
5. Consequences: what happens if I am wrong?
6. Question the question: was this the right question, and what does the reasoning so far tell me?

**The Five Whys** asks "why?" of a claim, then of the answer, repeatedly. A chain that ends in a measurement or a law has found a fact. A chain that ends in "because I said so", "that's how it's done" or "let's take it offline" has found an assumption. Record it as one rather than treating it as settled. Five is a habit, not a rule. Stop when you reach a fact or a dead end.

## Signals of analogy

When one of these shows up, return to step 4 for that claim.

| Signal | Move |
| --- | --- |
| "It's always been done this way" or "everyone does X" | Ask what fact makes X necessary here. |
| "Nobody has done that, so it won't work" | Separate "untried" from "violates a fact". Only the second rules it out. |
| "It has always cost / taken this much" | Price the floor from the constituents. |
| A plan sized to the worst case seen so far (the floodwall built for the last flood) | Size it to what the facts say could happen. |
| Reading everything because there is too much information | Find the three to five variables that move the outcome and track only those. |
| "We need to move first" | Check the evidence for this market. The iPhone was not first, it was better. |
| An answer that rests on gut feel or a strong reaction | Run the six Socratic questions on it. |
| An analogy used to argue rather than to explain | Keep it for communicating. Rebuild the argument from the facts. |

## Working note

Produce this, in the conversation or in a file if the user wants one. Keep it as short as the problem allows.

```markdown
## Goal
<one sentence, outcome only>

## Accepted answer
<the current approach>

## Claims
| Claim or part | Bin (fact / assumption) | Source or why-chain end |
| --- | --- | --- |

## Floor
<number and working, or why none>

## Options
| Option | Assumption it drops | What kills it | Cheapest test |
| --- | --- | --- | --- |

## Recommendation
<the option to test first and why>
```
