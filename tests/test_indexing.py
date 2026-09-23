from __future__ import annotations

import asyncio

import pytest

from rag_agent_blueprint.indexing.chunking import RecursiveTokenChunker
from rag_agent_blueprint.indexing.embeddings import EmbeddingClient
from rag_agent_blueprint.indexing.pipeline import index_document
from rag_agent_blueprint.indexing.vector_store import VectorStore


def test_recursive_token_chunker_raises_not_implemented():
    chunker = RecursiveTokenChunker()
    with pytest.raises(NotImplementedError):
        chunker.split("some document text")


def test_index_document_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        index_document(
            document_id="doc-1",
            full_text="some document text",
            chunker=None,
            embedder=None,
            store=None,
        )


def test_embedding_client_embed_raises_not_implemented():
    embedder = EmbeddingClient(client=None, model="stub-embedding-model", dimensions=768)
    with pytest.raises(NotImplementedError):
        embedder.embed(["some text"])


def test_vector_store_similarity_search_raises_not_implemented():
    store = VectorStore(connection=None)
    with pytest.raises(NotImplementedError):
        asyncio.run(store.similarity_search(query_embedding=[0.0], top_k=5))


def test_vector_store_similarity_search_scoped_raises_not_implemented():
    store = VectorStore(connection=None)
    with pytest.raises(NotImplementedError):
        asyncio.run(store.similarity_search(query_embedding=[0.0], top_k=5, document_id="doc-1"))


def test_vector_store_get_fragment_raises_not_implemented():
    store = VectorStore(connection=None)
    with pytest.raises(NotImplementedError):
        asyncio.run(store.get_fragment(document_id="doc-1", fragment_index=0))


def test_vector_store_get_representative_fragments_raises_not_implemented():
    store = VectorStore(connection=None)
    with pytest.raises(NotImplementedError):
        asyncio.run(store.get_representative_fragments(document_id="doc-1", k=5))
