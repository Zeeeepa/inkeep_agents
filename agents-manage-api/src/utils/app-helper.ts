import { OpenAPIHono } from '@hono/zod-openapi';
import type { ResolvedRef } from '@inkeep/agents-core';

export const createAppWithResolvedRef = (): OpenAPIHono<{ Variables: { resolvedRef: ResolvedRef | undefined } }> => {
  return new OpenAPIHono<{ Variables: { resolvedRef: ResolvedRef | undefined } }>();
};