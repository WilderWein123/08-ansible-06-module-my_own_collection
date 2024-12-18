#!/usr/bin/python

# Andrey Seregin
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module for Netology education

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: My test module creates file with some content.

options:
    path:
        description: This is path to the file, witch created by this module
        required: true
        type: str
    content:
        description: this is text message in the file 
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Andrey Seregin
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_own_module:
    path:'/root/my_own_collection/ansible/args.txt'
    content: 'Success!'

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'File has been created with my_own_module'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File created'
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        failed=False,
        original_message='file successfully created',
        message='file has been created with this my_own_module'
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
#   if module.check_mode:
#        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)

#    result['original_message'] = module.params['path']
 
#   result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result

#    if module.params['path'] == 'fail me':
#        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
#    module.exit_json(**result)

if module.check_mode:
        if not os.path.exists(module.params['path']):
            result['changed'] = True
        module.exit_json(**result)

    if not os.path.exists(module.params['path']):
        with open(module.params['path'], 'w') as f:
            f.write(module.params['content'])
        result['changed'] = True
        result['original_message'] = 'File created'
        result['message'] = 'File created'
    else:
        result['original_message'] = 'File is already exists'
        result['message'] = 'File is already exists'

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
