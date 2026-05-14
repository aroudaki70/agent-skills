# Performance Checklist

## Frontend
- [ ] Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1
- [ ] Bundle size budget: < 200KB initial JS
- [ ] Images: lazy loading, proper sizing, WebP format
- [ ] Code splitting for route-based chunks

## Backend
- [ ] Query optimization (N+1 detection, indexing)
- [ ] Caching strategy (Redis/CDN)
- [ ] Pagination for list endpoints
- [ ] Connection pooling for databases

## Measurement
- [ ] Profile before optimizing
- [ ] Use Lighthouse, WebPageTest for frontend
- [ ] Use APM (DataDog/NewRelic) for backend
- [ ] Establish performance budgets
