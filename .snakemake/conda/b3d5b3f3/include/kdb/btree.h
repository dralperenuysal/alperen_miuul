/*===========================================================================
*
*                            PUBLIC DOMAIN NOTICE
*               National Center for Biotechnology Information
*
*  This software/database is a "United States Government Work" under the
*  terms of the United States Copyright Act.  It was written as part of
*  the author's official duties as a United States Government employee and
*  thus cannot be copyrighted.  This software/database is freely available
*  to the public for use. The National Library of Medicine and the U.S.
*  Government have not placed any restriction on its use or reproduction.
*
*  Although all reasonable efforts have been taken to ensure the accuracy
*  and reliability of the software and data, the NLM and the U.S.
*  Government do not and cannot warrant the performance or results that
*  may be obtained by using this software or data. The NLM and the U.S.
*  Government disclaim all warranties, express or implied, including
*  warranties of performance, merchantability or fitness for any particular
*  purpose.
*
*  Please cite the author in any work or product based on this material.
*
* ===========================================================================
*
*/

#ifndef _h_kdb_btree_
#define _h_kdb_btree_

#ifndef _h_kdb_extern_
#include <kdb/extern.h>
#endif

#ifndef _h_klib_defs_
#include <klib/defs.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif


/*--------------------------------------------------------------------------
 * defines
 */


/*--------------------------------------------------------------------------
 * forwards
 */
struct KFile;

/*--------------------------------------------------------------------------
 * KBTree
 *  this implementation is an extremely simplified structure
 *  meant to provide the ability to create an index for temporary use
 */
typedef struct KBTree KBTree;


/* MakeRead
 * MakeUpdate
 *  make a b-tree object backed by supplied KFile
 *
 *  "backing" [ IN ] - open file with appropriate permissions:
 *   read is required in all cases, and write is required for update.
 *   NB - a reference will be attached to this file.
 *
 *  "climit" [ IN ] - cache limit in bytes. the internal cache will
 *   retain UP TO ( but not exceeding ) the limit specified. a value
 *   of 0 ( zero ) will disable caching.
 *
 *  "write_through" [ IN ] - if true, causes flushing of modified page
 *   after its value is released
 *
 *  "type" [ IN ] - describes the key type ( see above )
 *
 *  "key_chunk_size" [ IN ] - the "chunking" ( alignment ) factor for
 *   storing keys, rounded up to the nearest power of 2.
 *
 *  "value_chunk_size" [ IN ] - chunking factor for values
 *   ( see "key_chunk_size" )
 *
 *  "min_key_size" [ IN ] and "max_key_size" [ IN ] - specifies the allowed
 *   opaque key sizes. min == max implies fixed size. ignored for well
 *   known fixed size key types.
 *
 *  "id_size" [ IN ] - size of id in bytes, from 1 to 8.
 *
 *  "min_value_size" [ IN ] and "max_value_size" [ IN ] - specifies the allowed
 *   value sizes. min == max implies fixed size.
 *
 *  "cmp" [ IN, NULL OKAY ] - optional comparison callback function for opaque keys.
 *   specific key types will use internal comparison functions. for opaque keys, a
 *   NULL function pointer will cause ordering by size and binary comparison.
 */
KDB_EXTERN rc_t CC KBTreeMakeRead_1 ( const KBTree **bt,
                                     struct KFile const *backing, size_t climit);

KDB_EXTERN rc_t CC KBTreeMakeUpdate_1 ( KBTree **bt, struct KFile *backing,
    size_t climit );

#define KBTreeMakeRead(PBT, BACK, CLIM, CMP) KBTreeMakeRead_1(PBT, BACK, CLIM)

#define KBTreeMakeUpdate(PBT, BACK, CLIM, WT, T, MIN_KS, MAX_KS, ID_SIZE, CMP) \
    KBTreeMakeUpdate_1(PBT, BACK, CLIM)

/* AddRef
 * Release
 *  ignores NULL references
 */
KDB_EXTERN rc_t CC KBTreeAddRef ( const KBTree *self );
KDB_EXTERN rc_t CC KBTreeRelease ( const KBTree *self );


/* DropBacking
 *  used immediately prior to releasing
 *  prevents modified pages from being flushed to disk
 *  renders object nearly useless
 */
KDB_EXTERN rc_t CC KBTreeDropBacking ( KBTree *self );


/* Size
 *  returns size in bytes of file and cache
 *
 *  "lsize" [ OUT, NULL OKAY ] - return parameter for logical size
 *
 *  "fsize" [ OUT, NULL OKAY ] - return parameter for file size
 *
 *  "csize" [ OUT, NULL OKAY ] - return parameter for cache size
 */
KDB_EXTERN rc_t CC KBTreeSize ( const KBTree *self,
    uint64_t *lsize, uint64_t *fsize, size_t *csize );


/* Find
 *  searches for a match
 *
 *  "val" [ OUT ] - return parameter for value found
 *   accessed via KBTreeValueAccess* described above
 *   must be balanced with a call to KBTreeValueWhack.
 *
 *  "key" [ IN ] and "key_size" [ IN ] - describes an
 *   opaque key
 */
KDB_EXTERN rc_t CC KBTreeFind ( const KBTree *self, uint64_t *id,
    const void *key, size_t key_size );


/* Entry
 *  searches for a match or creates a new entry
 *
 *  "val" [ OUT ] - return parameter for value found
 *   accessed via KBTreeValueAccess* described above
 *   must be balanced with a call to KBTreeValueWhack.
 *
 *  "was_inserted" [ OUT ] - if true, the returned value was the result of an
 *   insertion and can be guaranteed to be all 0 bits. otherwise, the returned
 *   value will be whatever was there previously.
 *
 *  "alloc_size" [ IN ] - the number of value bytes to allocate upon insertion,
 *   i.e. if the key was not found. this value must agree with the limits
 *   specified in Make ( see above ).
 *
 *  "key" [ IN ] and "key_size" [ IN ] - describes an
 *   opaque key
 */
KDB_EXTERN rc_t CC KBTreeEntry ( KBTree *self, uint64_t *id,
    bool *was_inserted, const void *key, size_t key_size );


/* ForEach
 *  executes a function on each tree element
 *
 *  "reverse" [ IN ] - if true, iterate in reverse order
 *
 *  "f" [ IN ] and "data" [ IN, OPAQUE ] - callback function
 */
KDB_EXTERN rc_t CC KBTreeForEach ( const KBTree *self, bool reverse,
    void ( CC * f ) ( const void *key, size_t key_size, uint32_t id, void *data ), void *data );


#ifdef __cplusplus
}
#endif

#endif /*  _h_kdb_btree_ */
