import base64

code = 'Vmxkd1NrNVhVbk5qUlZKU1ltdGFjRlJYZEhOaWJFNVhWR3RPV0dKVmJEWldiR1JyV1ZkS1ZXRXphRnBpVkVaVFYycEtVMU5IUmtobFJYQlRUVmhDTmxZeFdtdGhhelZ5WWtWYWFWSlViRmRVVlZaYVRURmFjbFpyT1ZaV2JXUTJWa1pvYTFkck1YVlVhbHBoVWxack1GUlZaRXRqVmxaMVZHMTRXRkpVUlRCWFdIQkdUbGRHY2s1VmFFOVdNWEJoV1Zkek1XSldaSFJPVm1SclZsZDRXbFJWVm5wUVVUMDk='

for i in xrange(20):
    code = base64.b64decode(code)
    print code
