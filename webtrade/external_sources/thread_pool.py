from multiprocessing.dummy import Pool as ThreadPool

def thread_pool(worker,arg_list:list,n_threads:int)->tuple:
    true_results,false_results=[],[]
    pool = ThreadPool(n_threads)
    results=pool.map(worker,arg_list)
    pool.close()
    pool.join()
    
    for el in results:
        if el[0]:
            true_results.append([el[1],el[2]])
        else:
            false_results.append(el[0])
    return (true_results,false_results)