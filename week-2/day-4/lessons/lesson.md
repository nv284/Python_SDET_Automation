Implicit vs Explicit Waits, Expected Conditions, Dynamic UI, Flaky Tests

Concepts — beginner friendly:

- Implicit wait: tell the driver to wait a fixed time when searching for elements; a single setting that applies globally. In our simulation it means sleep before failing.
- Explicit wait: wait for a specific condition to become true by polling until a timeout. More reliable and focused.
- Expected conditions: reusable conditions (e.g., element visible, clickable) used with explicit waits.
- Handling dynamic UI: pages where elements are added/removed asynchronously; use retries, waits, and robust selectors.
- Flaky tests: tests that sometimes pass, sometimes fail; common causes include timing issues, test order dependencies, shared state, network flakiness.

Mitigation strategies:
- Prefer explicit waits for specific conditions
- Use stable selectors and cleanup test state
- Isolate tests and avoid shared global state
- Add retries for known transient failures and improve logging

See examples in `examples/` for runnable demos and detailed comments.
