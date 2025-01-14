#!/bin/env python3

import wftest as wt

def is_gui() -> bool:
    return True

class WTest(wt.WayfireTest):
    def prepare(self):
        return self.require_test_clients(['wleird-subsurfaces'])

    def _run(self):
        self.socket.run('wleird-subsurfaces nest-subsurfaces')
        self.wait_for_clients(2) # Wait for subsurfaces to start
        if error := self.take_screenshot('final'):
            return wt.Status.CRASHED, error
        return wt.Status.OK, None
