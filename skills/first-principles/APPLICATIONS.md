# First principles by domain

The domain branch of [`first-principles`](SKILL.md). Read the section for the work at hand. The steps in `SKILL.md` stay the same; this file supplies what the parts, facts and floors usually are in each domain.

## Engineering

Typical accepted answers: "we need microservices / Kubernetes / a queue", "this query can't get faster", "a rewrite takes six months", "we must support every legacy client".

- **Parts.** Requests, bytes, round trips, CPU time, storage, people-hours, the callers that depend on an interface.
- **Facts.** Measured latency and throughput, profiler output, row counts, hardware limits (disk and network bandwidth, memory), the actual list of callers from code search or logs, the SLA in the contract.
- **Floor.** The minimum work the task physically needs: bytes that must be read divided by bandwidth, the number of round trips the data dependency forces, the lines that must change. Compare it with what runs today.
- **Common assumptions to test.** "The framework requires it", "the other team needs this field", "traffic will grow 10x", "this is the industry standard architecture". Check each against code, logs or a written requirement.
- **Rebuild.** A design built from the measured load and the real callers, which is often smaller than the one copied from a larger company.

## Product

Typical accepted answers: "users want feature X", "competitor Y has it, so we need it", "conversion is capped at Z%", "this flow needs these steps".

- **Parts.** The job the user is trying to get done, each step of the flow, each field asked for, each decision the user must make.
- **Facts.** Behavioural data (funnels, session recordings, support tickets with counts), interview quotes, legal or payment requirements that force a step.
- **Floor.** The fewest steps and inputs the job needs once only the forced requirements remain. Every extra step is an assumption to justify.
- **Common assumptions to test.** A request taken as the need ("add a filter" when the need is "find the right option faster"), a competitor's feature taken as proof of demand, a metric taken as the goal.
- **Rebuild.** CD Baby is the pattern. Derek Sivers asked what a business needs and answered "happy customers", then spent on that and skipped what did not serve it: investors, offices, expensive systems. He built office computers from parts for $1,000 where funded peers spent $100,000 "because we need the very best", which did nothing for customers.

## Strategy

Typical accepted answers: "we must move first", "all the good ideas are taken", "margins in this market are always thin", "it's never been done".

- **Parts.** The cost stack, the value chain, the customer's budget and alternatives, distribution, the three to five variables that decide the outcome.
- **Facts.** Input costs at market prices, unit economics from real data, the customer's measured willingness to pay, regulation.
- **Floor.** The cost or price the inputs allow, built bottom-up, compared with the market's accepted price.
- **Common assumptions to test.** First-mover advantage (first movers fail more often than latecomers; Microsoft won on business model, not on being first), "the market is saturated", plans sized to the worst case seen so far rather than what could happen.
- **Rebuild.** BuzzFeed is the pattern. Jonah Peretti decided the first principle of a successful site was wide distribution, so he made content people want to share rather than content built for search engines, and measured it with A/B tests.

## Worked examples from the article

**SpaceX.** Goal: send people to Mars, which needs much cheaper rockets. Decomposition: aerospace-grade aluminium alloys, titanium, copper, carbon fibre. Floor: the materials cost about 2% of a rocket's typical price. Conclusion: the price came from convention and process, not from physics, so building rockets from scratch was worth testing.

**Battery packs.** Accepted answer: $600 per kWh, and it will stay near that. Decomposition: cobalt, nickel, aluminium, carbon, polymers for separation, a steel can. Floor: about $80 per kWh at London Metal Exchange spot prices. Conclusion: the work is finding cheaper ways to combine the materials into a cell.

**Investors and information.** One group reads every press release and article and fears missing something. The other identifies the three to five variables that move an investment and follows only those. The second group decomposed "stay informed" into the facts that matter.

**Memory.** "I don't have a good memory" is a belief. The fact is that the brain can store far more than people assume, so the problem becomes finding the best way to store information.
